# from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView

from flow.models import WorkFlowData, WorkFlowImage, WorkFlowComment
from flow.serializers.workflowdata import (
    WorkFlowDataSerializer,
    WorkFlowCommentSerializer,
)
from urllib.parse import urljoin
import urllib.parse

import requests
from django.urls import reverse
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from wechat_django.oauth.client import WeChatOAuthClient
from wechat_django.models import WeChatApp
import json
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView


from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.core.cache import cache
from django.http import JsonResponse


def send_message_to_client(request, channel_name):
    # 从缓存中获取存储的 channel_name
    stored_channel_name = cache.get(channel_name)

    if stored_channel_name:
        # 获取channel layer
        channel_layer = get_channel_layer()

        # 发送消息到特定客户端的channel_name
        async_to_sync(channel_layer.send)(
            stored_channel_name,
            {
                "type": "send.message",  # 消息类型，用于调用 send_message
                "message": {
                    "text": f"Hello, this is a message for channel {stored_channel_name}"
                },
            },
        )

        return JsonResponse(
            {"status": f"Message sent to client with channel {stored_channel_name}"}
        )
    else:
        return JsonResponse({"status": "Client not found"}, status=404)


class UploadAPIView(APIView):
    """
    处理来自前端的 postData 上传，并根据 techsid 和 r 值执行不同的逻辑
    """

    def post(self, request):
        # 获取 URL 中的参数 techsid 和 r
        r_value = request.GET.get("r")
        techsid = request.GET.get("techsid")
        client_id = request.GET.get("client_id")

        if not r_value or not techsid:
            return Response(
                {"error": "Missing 'r' or 'techsid' in URL"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # 根据 r 的值执行不同的逻辑
        if r_value == "comfyui.apiv2.upload":
            if not techsid:
                return Response(
                    {"errno": 41009, "message": "用户未登陆", "data": []},
                    status=status.HTTP_200_OK,
                )
            # 解析表单中的 json_data
            json_data = request.POST.get("json_data", None)

            if not json_data:
                return Response(
                    {"error": "Missing json_data"}, status=status.HTTP_400_BAD_REQUEST
                )

            try:
                post_data = json.loads(json_data)  # 解析 json_data
            except json.JSONDecodeError:
                return Response(
                    {"error": "Invalid JSON data"}, status=status.HTTP_400_BAD_REQUEST
                )
            cs_img_files = request.FILES.getlist("cs_img_files", [])
            return self.handle_upload(post_data, client_id, techsid, cs_img_files)
        elif r_value == "comfyui.apiv2.code":
            return self.handle_code_logic(request.data, techsid)
        else:
            return Response(
                {"error": f"Unsupported r value: {r_value}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def handle_upload(self, post_data, client_id, techsid, cs_img_files):
        """
        处理上传逻辑，并将数据保存到数据库
        """
        post_data = post_data.get("postData")
        try:
            # 创建 PostData 实例并保存
            post_data_instance = WorkFlowData.objects.create(
                techsid=techsid,
                res_node=post_data.get("res_node"),
                main_images=post_data.get("mainImages", []),
                title=post_data.get("title"),
                gn_desc=post_data.get("gn_desc"),
                sy_desc=post_data.get("sy_desc"),
                fee=post_data.get("fee"),
                free_times=post_data.get("free_times"),
                uniqueid=post_data.get("uniqueid"),
                client_id=client_id,
                output=post_data.get("output", {}),
                workflow=post_data.get("workflow", {}),
                post_data=post_data,
            )

            # 处理图片节点上传
            cs_img_descs = post_data.get("cs_img_nodes", [])

            for index, img_file in enumerate(cs_img_files):
                desc = (
                    cs_img_descs[index].get("desc", "")
                    if index < len(cs_img_descs)
                    else ""
                )
                WorkFlowImage.objects.create(
                    post_data=post_data_instance, image=img_file, desc=desc
                )

            r = {
                "errno": 1,
                "message": "OK",
                "data": {
                    "data": {
                        "message": "更新成功",
                        "code": 1,
                        "list": [
                            {
                                "code": "https://tt-1254127940.file.myqcloud.com/tech_huise/66/code/ONZgL75MhOrqVE6F.png",
                                "desc": "微信小程序页面",
                            },
                            {
                                "code": "https://tt-1254127940.file.myqcloud.com/tech_huise/66/code/euWO8Wl7gnc1lkRK.png",
                                "desc": "抖音小程序页面",
                            },
                            {
                                "code": "https://tt-1254127940.file.myqcloud.com/tech_huise/66/code/6LCGwiQNRj152DZw1728990819.png",
                                "desc": "H5页面",
                            },
                            {
                                "code": "https://tt-1254127940.file.myqcloud.com/images/66/2024/05/h8kBOfzsOs4ee0UEP1Pp0OeySJMOFk.jpg",
                                "desc": "手机端后台",
                            },
                        ],
                        "name": post_data.get("uniqueid"),
                        "gameid": "3311",
                    }
                },
            }

            return Response(r, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def handle_code_logic(self, post_data, techsid):
        """
        处理与 code 相关的逻辑
        """
        postData = post_data.get("postData")
        if postData.get("s_key"):
            r = {
                "errno": 0,
                "message": "OK",
                "data": {
                    "data": {"code": 1, "data": {"techsid": "init", "openid": "init"}}
                },
            }
            return Response(r, status=status.HTTP_200_OK)
        else:
            r = {
                "errno": 0,
                "message": "OK",
                "data": {
                    "data": {
                        "code": 1,
                        "data": "https://tt-1254127940.file.myqcloud.com/tech_huise/66/code/qPVkSBxOnfwDlpNT.png",
                        "desc": "请微信扫码登录",
                        "test": {"s_key": "", "subdomain": "ef28c7ddcc72"},
                        "s_key": "wx1729222221733JsDThh",
                    }
                },
            }
            return Response(r, status=status.HTTP_200_OK)


class WorkFlowListView(ListAPIView):

    def get(self, request):
        flows = WorkFlowData.objects.all()
        serializer = WorkFlowDataSerializer(flows, many=True)
        return Response(serializer.data)


class WorkFlowDetailView(RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        flows = WorkFlowData.objects.get(id=id)
        serializer = WorkFlowDataSerializer(flows)
        return Response(serializer.data)


class WorkFlowCommentList(ListCreateAPIView):

    def get(self, request, *args, **kwargs):
        workflow_id = kwargs.get('workflow_id')
        flow = WorkFlowData.objects.filter(id=workflow_id).first()
        if flow:
            comments = WorkFlowComment.objects.filter(workflow=flow).order_by('-created').all()
            serializer = WorkFlowCommentSerializer(comments, many=True)
            return Response({'data': serializer.data})
        return Response({'data': []})

    def post(self, request, *args, **kwargs):
        workflow_id = kwargs.get('workflow_id')
        flow = WorkFlowData.objects.filter(id=workflow_id).first()
        text = request.data.get('comment')
        comment = WorkFlowComment(
            workflow=flow,
            comment=text
        )
        comment.save()
        serializer = WorkFlowCommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class WechatQRLogin(APIView):

    def get(self, request):
        app = WeChatApp.objects.get_by_name("现金宝H5")
        url = app.build_url("wechat_callback")
        cfg = app.configurations
        redirect = cfg.get("SITE_HOST")
        client = WeChatOAuthClient(app)
        url = client.qrconnect_url(redirect_uri=redirect, state="STATE")
        return Response({"url": url}, status=status.HTTP_200_OK)


class WechatMinAppLogin(APIView):

    def post(self, request):
        app = WeChatApp.objects.get_by_name("现金宝")
        code = request.data.get("code")
        user, data = app.auth(code)
        return Response({"data": data}, status=status.HTTP_200_OK)


class WechatCallback(APIView):
    url_name = "wechat_callback"

    def get(self, request):
        return Response({}, status=status.HTTP_200_OK)


class GoogleLoginUrl(APIView):
    def get(self, request, *args, **kwargs):
        """
        If you are building a fullstack application (eq. with React app next to Django)
        you can place this endpoint in your frontend application to receive
        the JWT tokens there - and store them in the state
        """
        client_id = settings.GOOGLE_OAUTH_CLIENT_ID
        callback_url = urllib.parse.quote_plus(urljoin("http://aidep.cn:8601", reverse("flow_google_callback")))
        return Response(
            {
                'url': f'https://accounts.google.com/o/oauth2/v2/auth?redirect_uri={callback_url}&prompt=consent&response_type=code&client_id={client_id}&scope=openid%20email%20profile&access_type=online'
            },
            status=status.HTTP_200_OK
        )


class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = settings.GOOGLE_OAUTH_CALLBACK_URL
    client_class = OAuth2Client


class GoogleCallback(APIView):

    def get(self, request, *args, **kwargs):
        code = request.GET.get("code")
        if code is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        token_endpoint_url = urljoin("http://aidep.cn:8601", reverse("flow_google_login"))
        response = requests.post(url=token_endpoint_url, data={"code": code})
        print(response)
        return Response(response.json(), status=status.HTTP_200_OK)

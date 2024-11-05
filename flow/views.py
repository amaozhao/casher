import json
import string, random
import urllib.parse
from urllib.parse import urljoin

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.core.cache import cache
from django.urls import reverse
from django.http import JsonResponse
from django.conf import settings
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from flow.models import WorkFlowComment, WorkFlowData, WorkFlowImage
from flow.serializers.workflowdata import (
    WorkFlowCommentSerializer,
    WorkFlowDataSerializer,
)
from wxapp.service import generate_mp_qr_code as c_generate_mp_qr_code
from wxappb.service import generate_mp_qr_code as b_generate_mp_qr_code
from wxappb.models import WxAppBTechs
from flow.service import generate_h5_qr_code

chars = string.ascii_letters + string.digits


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
            # 解析表单中的 json_data
            json_data = request.POST.get("json_data", None)
            techsid = request.POST.get("techsid", None)
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
            mainImages = request.FILES.getlist("mainImages", [])
            return self.handle_upload(post_data, client_id, techsid, mainImages)
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
        techsid = post_data.get("techsid")
        if techsid in ('init', '', None):
            return Response(
                {
                    "errno": 41009,
                    "message": "用户未登陆"
                }
            )
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
            # cs_img_descs = post_data.get("cs_img_nodes", [])

            for index, img_file in enumerate(cs_img_files):
                WorkFlowImage.objects.create(
                    workflow=post_data_instance, image=img_file
                )

            h5_c_image = generate_h5_qr_code(workflow_id=post_data_instance.id, web_type='c')
            wxp_c_image = c_generate_mp_qr_code(
                f'/web/workflow/workflow_id={post_data_instance.id}/',
                query={"workflow_id": post_data_instance.id}
            )
            wxp_b_image = b_generate_mp_qr_code(
                f'/web-b/workflow/workflow_id={post_data_instance.id}/',
                query={"workflow_id": post_data_instance.id}
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
                                "code": wxp_c_image,
                                "desc": "微信小程序页面",
                            },
                            {
                                "code": h5_c_image,
                                "desc": "H5页面",
                            },
                            {
                                "code": wxp_b_image,
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

    def get_google_login_url(self, techsid):
        client_id = settings.GOOGLE_OAUTH_CLIENT_ID
        callback_url = urllib.parse.quote_plus(
            urljoin("http://aidep.cn", reverse("google_callback"))
        )
        state = {"techsid": techsid}
        url = (
            f"https://accounts.google.com/o/oauth2/v2/auth?redirect_uri={callback_url}&"
            f"prompt=consent&response_type=code&client_id={client_id}&"
            f"scope=openid%20email%20profile&access_type=online&"
            f"state={urllib.parse.quote_plus(json.dumps(state))}"
        )
        return url

    def handle_code_logic(self, post_data, techsid):
        """
        处理与 code 相关的逻辑
        """
        postData = post_data.get("postData")
        wx_tech = WxAppBTechs.objects.filter(techsid=techsid).first()
        if wx_tech:
            techsid = wx_tech.techsid
        if postData.get("s_key"):
            r = {
                "errno": 0,
                "message": "OK",
                "data": {
                    "data": {
                        "code": 0,
                        'data': {
                            "techsid": 'wQMWPR7m'
                        }
                    }
                },
            }
            return Response(r, status=status.HTTP_200_OK)
        else:
            s_key = ''.join(random.choice(chars) for _ in range(8))
            qrcode = b_generate_mp_qr_code(path='/', query={'techsid': s_key})
            r = {
                "errno": 0,
                "message": "OK",
                "data": {
                    "data": {
                        "code": 1,
                        "data": qrcode,
                        "desc": f"请微信扫码/<a href='{self.get_google_login_url(s_key)}'>Google</a>登录",
                        "test": {"s_key": s_key, "subdomain": "11"},
                        "s_key": s_key,
                        "techsid": s_key,
                        "google_log_url": self.get_google_login_url(s_key)
                    }
                }
            }
            return Response(r, status=status.HTTP_200_OK)


class WorkFlowListView(ListAPIView):
    authentication_classes = []
    def get(self, request):
        flows = WorkFlowData.objects.all()
        serializer = WorkFlowDataSerializer(flows, many=True)
        return Response({"data": serializer.data, "status": status.HTTP_200_OK})

    def get_queryset(self):
        return WorkFlowData.objects.all()


class BWorkFlowListView(ListAPIView):
    authentication_classes = []
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            techs_ids = WxAppBTechs.objects.filter(user=user).all()
            flows = WorkFlowData.objects.filter(techsid__in=[t.techsid for t in techs_ids])
        else:
            flows = WorkFlowData.objects.all()
        serializer = WorkFlowDataSerializer(flows, many=True)
        return Response({"data": serializer.data, "status": status.HTTP_200_OK})

    def get_queryset(self):
        user = self.request.user
        return WorkFlowData.objects.firter(user=user)


class BWorkFlowDetailView(ListAPIView):

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        flows = WorkFlowData.objects.get(id=id)
        serializer = WorkFlowDataSerializer(flows)
        return Response({"data": serializer.data, "status": status.HTTP_200_OK})


class WorkFlowDetailView(RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        flows = WorkFlowData.objects.get(id=id)
        serializer = WorkFlowDataSerializer(flows)
        return Response({"data": serializer.data, "status": status.HTTP_200_OK})


class WorkFlowCommentList(ListCreateAPIView):
    serializer_class = WorkFlowCommentSerializer

    def get(self, request, *args, **kwargs):
        workflow_id = kwargs.get("workflow_id")
        flow = WorkFlowData.objects.filter(id=workflow_id).first()
        if flow:
            comments = (
                WorkFlowComment.objects.filter(workflow=flow).order_by("-created").all()
            )
            serializer = WorkFlowCommentSerializer(comments, many=True)
            return Response({"data": serializer.data, "status": status.HTTP_200_OK})
        return Response({"data": [], "status": status.HTTP_200_OK})

    def post(self, request, *args, **kwargs):
        workflow_id = request.data.get('workflow_id')
        flow = WorkFlowData.objects.filter(id=workflow_id).first()
        text = request.data.get("comment")
        comment = WorkFlowComment(workflow=flow, comment=text)
        comment.save()
        serializer = WorkFlowCommentSerializer(comment)
        return Response(
            {
                "data": serializer.data,
                "status": status.HTTP_201_CREATED,
                "message": "投诉成功"
            },
            status=status.HTTP_201_CREATED,
        )

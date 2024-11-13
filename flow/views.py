import json
import random
import string
import urllib.parse
from urllib.parse import urljoin

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.conf import settings
from django.core.cache import cache
from django.http import JsonResponse
from django.urls import reverse
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from flow.models import WorkFlowBanner, WorkFlowComment, WorkFlowData, WorkFlowImage
from flow.serializers.workflowdata import (
    WorkFlowCommentSerializer,
    WorkFlowDataSerializer,
    BWorkFlowDataSerializer,
)
from wxapp.service import generate_mp_qr_code as c_generate_mp_qr_code
from wxappb.models import AuthorTechs
from wxappb.service import generate_mp_qr_code as b_generate_mp_qr_code

chars = string.ascii_letters + string.digits


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
            return self.handle_upload(post_data, client_id, mainImages)
        elif r_value == "comfyui.apiv2.code":
            return self.handle_code_logic(request.data, techsid)
        else:
            return Response(
                {"error": f"Unsupported r value: {r_value}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def handle_upload(self, post_data, client_id, cs_img_files):
        """
        处理上传逻辑，并将数据保存到数据库
        """
        post_data = post_data.get("postData")
        techsid = post_data.get("techsid")
        if techsid in ("init", "", None):
            return Response({"errno": 41009, "message": "用户未登陆"})
        try:
            from task.models import TaskFreeCount

            # 创建 PostData 实例并保存
            workflow = WorkFlowData.objects.filter(
                uniqueid=post_data.get("uniqueid")
            ).first()
            if not workflow:
                workflow = WorkFlowData.objects.create(
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
            else:
                workflow.techsid = post_data.get("techsid")
                workflow.client_id = client_id
                workflow.title = post_data.get("title")
                workflow.gn_desc = post_data.get("gn_desc")
                workflow.sy_desc = post_data.get("sy_desc")
                workflow.output = post_data.get("output")
                workflow.workflow = post_data.get("workflow")
                workflow.fee = post_data.get("fee")
                workflow.free_times = post_data.get("free_times")
                if post_data.get("post_data"):
                    workflow.post_data = post_data.get("post_data")
                workflow.save()
            TaskFreeCount.objects.get_or_create(
                workflow=workflow, free_count=post_data.get("free_times") or 0
            )

            # 处理图片节点上传
            # cs_img_descs = post_data.get("cs_img_nodes", [])
            WorkFlowImage.objects.filter(workflow=workflow).delete()
            for index, img_file in enumerate(cs_img_files):
                WorkFlowImage.objects.create(workflow=workflow, image=img_file)
            wx_tech = AuthorTechs.objects.filter(techsid=techsid).first()
            provider = wx_tech.provider
            wxp_c_image = None
            wxp_b_image = None
            if provider != "google":
                wxp_c_image = c_generate_mp_qr_code(
                    f"/web/workflow/workflow_id={workflow.id}/",
                    query={"workflow_id": workflow.id},
                )
                wxp_b_image = b_generate_mp_qr_code(query={"techsid": techsid})
            html = self.get_app_html(wxp_c_image, wxp_b_image, workflow.id, provider)

            r = {
                "errno": 1,
                "message": "OK",
                "data": {
                    "data": {
                        "message": "更新成功",
                        "code": 1,
                        "name": post_data.get("uniqueid"),
                        "html": html,
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
            urljoin("https://aidep.cn", reverse("google_callback"))
        )
        state = {"techsid": techsid, "only_login": 1}
        url = (
            f"https://accounts.google.com/o/oauth2/v2/auth?redirect_uri={callback_url}&"
            f"prompt=consent&response_type=code&client_id={client_id}&"
            f"scope=openid%20email%20profile&access_type=online&"
            f"state={urllib.parse.quote_plus(json.dumps(state))}"
        )
        return url

    def get_weixin_login_url(self, techsid):
        redirect_uri = urllib.parse.quote_plus(
            urljoin("https://aidep.cn", reverse("weixin_callback"))
        )
        state = {"techsid": techsid, "only_login": 1}
        url = (
            f"https://open.weixin.qq.com/connect/qrconnect?"
            f"appid={settings.SOCIALACCOUNT_PROVIDERS['weixin']['APP']['client_id']}"
            f"&redirect_uri={redirect_uri}"
            f"&response_type=code"
            f"&scope=snsapi_login"
            f"&state={urllib.parse.quote_plus(json.dumps(state))}#wechat_redirect"  # 可设置自定义state参数
        )
        return url

    def get_login_html(self, s_key, qrcode):
        languestr = self.request.headers.get("languestr")
        google_login = "使用 Google 登录"
        if languestr == "en":
            google_login = "Login with Google"
        html = f"""
        <style type="text/css">
			body {{
				background-color: #161622;
				text-align: center;
			}}

			.login_text {{
				margin: 50px 0;
				height: 42px;
				font-size: 36px;
				color: #ffffff;
				line-height: 42px;
			}}

			.qrcode {{
				width: 280px;
				height: 280px;
				margin-top: 40px;
				border-radius: 16px;
			}}

			.bottomLine {{
				display: flex;
				width: 325px;
				margin: 40px auto;
				align-items: center;
			}}

			.divider_line {{
				flex-grow: 1;
				border-bottom: 1px solid #5b5b5b;
				border-image: linear-gradient(90deg, rgba(91, 91, 91, 1), rgba(37, 37, 37, 1)) 2 2;
			}}

			.divider_text {{
				margin: 0 10px;
				font-size: 12px;
				color: #dcdcdc;
			}}

			.other_login_div {{
				display: block;
				margin: 10px auto;
				width: 325px;
				height: 91px;
				background: #2c2c3a;
				border-radius: 16px;
			}}

			.other_login_text {{
				/* margin-top: 7px; */
				font-size: 12px;
				color: #fff;
			}}

			.logo_img {{
				width: 28px;
				height: 28px;
				margin-top: 20px;
			}}

			.btn_div {{
				width: 325px;
				line-height: 34px;
				background: #019083;
				border-radius: 16px;
				margin: auto;
				color: #fff;
				margin-top: 40px;
			}}
		</style>
        <img class="qrcode" src="{qrcode}" />
        <div class="bottomLine">
            <div class="divider_line"></div>
            <div class="divider_text">或</div>
            <div class="divider_line"></div>
        </div>
        <a class="other_login_div" id="google" style="text-decoration: none;" href="javascript:window.open('{self.get_google_login_url(s_key)}', 'GoogleLoginPopup', 'width=600,height=800,top='+(window.innerHeight-800)/2+',left='+(window.innerWidth-600)/2+',scrollbars=yes');">
            <img class="logo_img" src="data:image/svg+xml,%3csvg%20width='28'%20height='29'%20viewBox='0%200%2028%2029'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M6.28523%2011.6527C7.39816%208.28037%2010.5673%205.85837%2014.3212%205.85837C16.339%205.85837%2018.1616%206.57439%2019.5937%207.74607L23.7596%203.58011C21.221%201.36695%2017.9664%200%2014.3212%200C8.67659%200%203.8168%203.22007%201.48047%207.93595L6.28523%2011.6527Z'%20fill='%23EA4335'/%3e%3cpath%20d='M19.1424%2021.4954C17.8418%2022.3352%2016.1892%2022.7823%2014.3203%2022.7823C10.5808%2022.7823%207.42153%2020.3788%206.29721%2017.0266L1.47656%2020.6868C3.80999%2025.4109%208.66966%2028.6407%2014.3203%2028.6407C17.8202%2028.6407%2021.1647%2027.3964%2023.6694%2025.06L19.1424%2021.4954Z'%20fill='%2334A853'/%3e%3cpath%20d='M23.6694%2025.0601C26.2888%2022.6167%2027.9898%2018.9788%2027.9898%2014.3203C27.9898%2013.4741%2027.8597%2012.5628%2027.6644%2011.7166H14.3203V17.2495H22.0013C21.6223%2019.11%2020.605%2020.5511%2019.1424%2021.4955L23.6694%2025.0601Z'%20fill='%234A90E2'/%3e%3cpath%20d='M6.2974%2017.027C6.0126%2016.1778%205.85837%2015.2678%205.85837%2014.3205C5.85837%2013.3877%206.00795%2012.4909%206.28453%2011.6528L1.47977%207.93604C0.521011%209.85785%200%2012.0238%200%2014.3205C0%2016.6113%200.530789%2018.772%201.47675%2020.6872L6.2974%2017.027Z'%20fill='%23FBBC05'/%3e%3c/svg%3e" />
            <span id="google-login-url" class="other_login_text">{google_login}</span>
        </a>
        """
        return html

    def get_app_html(self, wxp_c_image, wxp_b_image, workflow_id, provider):
        if provider == "google":
            html = f"""
                    <style type="text/css">
            			body {{
            				background-color: #161622;
            				text-align: center;
            				color: #fff;
            			}}

            			.login_text {{
            				margin: 50px 0;
            				height: 42px;
            				font-size: 36px;
            				color: #ffffff;
            				line-height: 42px;
            			}}

            			.qrcode {{
            				width: 280px;
            				height: 280px;
            				margin-top: 40px;
            				border-radius: 20px;
            			}}

            			.mgT10 {{
            				margin-top: 10px;
            			}}

            			.content {{
            				width: 888px;
            				margin: auto;
            				display: flex;
            				justify-content: space-between;
            			}}
            		</style>
                    <div class="content">
            			<div>
            				<div class="login_text">用户端URL</div>
            				<div>URL:
            					<a style="color: #6AE1D6;" href="https://aidep.cn/web/?workflow_id={workflow_id}" target="_blank">
            					    https://aidep.cn/web/?workflow_id={workflow_id}
            					</a>
            				</div>
            			</div>
            			<div>
            				<div class="login_text">商户端URL</div>
            				<div>URL:
            					<a style="color: #6AE1D6;" href="https://aidep.cn/web-b/" target="_blank">https://aidep.cn/web-b/</a>
            				</div>
            			</div>
            		</div>
                    """
            return html
        html = f"""
        <style type="text/css">
			body {{
				background-color: #161622;
				text-align: center;
				color: #fff;
			}}

			.login_text {{
				margin: 50px 0;
				height: 42px;
				font-size: 36px;
				color: #ffffff;
				line-height: 42px;
			}}

			.qrcode {{
				width: 280px;
				height: 280px;
				margin-top: 40px;
				border-radius: 20px;
			}}

			.mgT10 {{
				margin-top: 10px;
			}}

			.content {{
				width: 666px;
				margin: auto;
				display: flex;
				justify-content: space-between;
			}}
		</style>
        <div class="content">
			<div>
				<div class="login_text">用户端URL</div>
				<div>URL:
					<a style="color: #6AE1D6;" href="https://aidep.cn/web/?workflow_id={workflow_id}">
					    https://aidep.cn/web/?workflow_id={workflow_id}
					</a>
				</div>
				<img class="qrcode" src="{wxp_c_image}" />
				<div class="mgT10">微信小程序</div>
			</div>
			<div>
				<div class="login_text">商户端URL</div>
				<div>URL:
					<a style="color: #6AE1D6;" href="https://aidep.cn/web-b/">https://aidep.cn/web-b/</a>
				</div>
				<img class="qrcode" src="{wxp_b_image}" />
				<div class="mgT10">商家后台</div>
			</div>
		</div>
        """
        return html

    def handle_code_logic(self, post_data, techsid):
        """
        处理与 code 相关的逻辑
        """
        postData = post_data.get("postData")
        wx_tech = AuthorTechs.objects.filter(techsid=postData.get("s_key")).first()
        if wx_tech:
            techsid = wx_tech.techsid
        if postData.get("s_key") and wx_tech:
            r = {
                "errno": 1,
                "message": "OK",
                "data": {
                    "data": {
                        "code": 1,
                        "techsid": techsid,
                        "data": {"techsid": techsid},
                    }
                },
            }
            return Response(r, status=status.HTTP_200_OK)
        else:
            s_key = "".join(random.choice(chars) for _ in range(8))
            qrcode = b_generate_mp_qr_code(query={"techsid": s_key})
            r = {
                "errno": 0,
                "message": "OK",
                "data": {
                    "data": {
                        "code": 1,
                        "data": qrcode,
                        "desc": "",
                        "html": self.get_login_html(s_key, qrcode),
                        "js": "",
                        "test": {"s_key": s_key, "subdomain": "11"},
                        "s_key": s_key,
                        "techsid": "init",
                        "google_log_url": self.get_google_login_url(s_key),
                    }
                },
            }
            return Response(r, status=status.HTTP_200_OK)


class WorkFlowListView(ListAPIView):
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        workflow_id = request.GET.get("workflow_id")
        if workflow_id:
            current_flow = WorkFlowData.objects.get(id=workflow_id, deleted=False)
            if not current_flow:
                return Response(
                    {
                        "data": [],
                        "message": "工作流未找到",
                        "status": status.HTTP_400_BAD_REQUEST,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            flows = WorkFlowData.objects.exclude(id=workflow_id, deleted=False).all()
            serializer = WorkFlowDataSerializer(flows, many=True)
            current_serializer = WorkFlowDataSerializer(current_flow)
            data = serializer.data
            data.insert(0, current_serializer.data)
            return Response({"data": data, "status": status.HTTP_200_OK})
        flows = WorkFlowData.objects.all()
        serializer = WorkFlowDataSerializer(flows, many=True)
        return Response({"data": serializer.data, "status": status.HTTP_200_OK})

    def get_queryset(self):
        return WorkFlowData.objects.all()


class BWorkFlowListView(ListAPIView):
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            techs_ids = AuthorTechs.objects.filter(user=user).all()
            flows = WorkFlowData.objects.filter(
                techsid__in=[t.techsid for t in techs_ids],
                deleted=False,
                status='online',
            )
        else:
            flows = WorkFlowData.objects.all()
        serializer = BWorkFlowDataSerializer(flows, many=True)
        return Response({"data": serializer.data, "status": status.HTTP_200_OK})

    def get_queryset(self):
        user = self.request.user
        return WorkFlowData.objects.firter(user=user)


class BWorkFlowDetailView(ListAPIView):
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        flows = WorkFlowData.objects.get(id=id)
        serializer = WorkFlowDataSerializer(flows)
        return Response({"data": serializer.data, "status": status.HTTP_200_OK})


class WorkFlowDetailView(RetrieveAPIView):
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        flow = WorkFlowData.objects.get(id=id)
        if flow.fee > 0:
            return Response(
                {"data": {}, "status": status.HTTP_200_OK},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        serializer = WorkFlowDataSerializer(flow)
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
        workflow_id = request.data.get("workflow_id")
        flow = WorkFlowData.objects.filter(id=workflow_id).first()
        text = request.data.get("comment")
        comment = WorkFlowComment(workflow=flow, comment=text)
        comment.save()
        serializer = WorkFlowCommentSerializer(comment)
        return Response(
            {
                "data": serializer.data,
                "status": status.HTTP_201_CREATED,
                "message": "投诉成功",
            },
            status=status.HTTP_201_CREATED,
        )


class WorkFlowBannerView(APIView):
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        banner = WorkFlowBanner.objects.first()
        if not banner:
            return Response({"data": {}, "status": status.HTTP_200_OK})
        if not banner.is_visible:
            return Response({"data": {}, "status": status.HTTP_200_OK})
        return Response(
            {
                "data": {"id": banner.id, "url": banner.url, "desc": banner.desc},
                "status": status.HTTP_200_OK,
            }
        )

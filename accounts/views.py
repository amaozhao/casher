import json
import urllib.parse
from urllib.parse import urljoin
from django.utils.http import urlencode

import requests
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.weixin.client import WeixinOAuth2Client
from allauth.socialaccount.providers.weixin.views import WeixinOAuth2Adapter
from allauth.socialaccount.models import SocialAccount
from dj_rest_auth.registration.views import SocialLoginView
from invitation.models import InvitationCode, InvitationRelation
from wxappb.models import AuthorTechs


class WXQRCodeAPIView(APIView):
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        # 设置微信扫码登录的 URL，并传入相应的参数
        client_type = request.GET.get('client_type')
        redirect_uri = urllib.parse.quote_plus(
            urljoin("https://aidep.cn", reverse("weixin_callback"))
        )
        workflow_id = request.GET.get('workflow_id')
        state = {"client_type": client_type}
        if workflow_id:
            state["wf_id"] = workflow_id
        state = urllib.parse.quote_plus(urllib.parse.quote_plus(json.dumps(state)))
        wechat_qr_url = (
            f"https://open.weixin.qq.com/connect/qrconnect?"
            f"appid={settings.WEIXINB_H5_APPID}"
            f"&redirect_uri={redirect_uri}"
            f"&response_type=code"
            f"&scope=snsapi_login"
            f"&state={state}#wechat_redirect"  # 可设置自定义state参数
        )

        # 直接将微信提供的二维码URL返回给前端
        return Response(
            {"status": status.HTTP_200_OK, "data": {"qr_url": wechat_qr_url}},
            status=status.HTTP_200_OK,
        )


class WXLoginAPIView(SocialLoginView):
    adapter_class = WeixinOAuth2Adapter
    callback_url = settings.WEIXIN_OAUTH_CALLBACK_URL
    client_class = WeixinOAuth2Client


class WXCallback(APIView):
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        code = request.GET.get("code")
        state = request.GET.get("state")
        if code is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        token_endpoint_url = urljoin("https://aidep.cn", reverse("weixin_login"))
        response = requests.post(
            url=token_endpoint_url, data={"code": code}, timeout=60, verify=False
        )
        res_json = response.json()
        user = res_json.get("user")
        if user:
            # 提交数据到GPU平台换取token，并保存
            if state:
                user = User.objects.get(id=user.get("pk"))
                state = urllib.parse.unquote_plus(state)
                state = json.loads(state)
                if state.get("client_type"):
                    wf_id = state.get('wf_id')
                    token = res_json.get("access")
                    if state.get("client_type") == 'c':
                        return redirect(f"https://aidep.cn/web/?workflow_id={wf_id}&token={token}")
                    return redirect(f"https://aidep.cn/web-b/?token={token}")
                techsid = state.get("techsid")
                if techsid:
                    AuthorTechs.objects.create(
                        user=user, techsid=techsid, provider="weixin"
                    )
                invite = state.get("invite")
                if invite:
                    inviter = InvitationCode.objects.filter(code=invite).first()
                    if inviter:
                        InvitationRelation.objects.create(
                            inviter=inviter.inviter, invitee=user
                        )
                        inviter.accepted = True
                        inviter.save()
                token = res_json.get("access")
                return redirect(f"https://aidep.cn/web-b/?token={token}")

        token = res_json.get("access")

        return redirect(f"https://aidep.cn/web/?token={token}")


class GoogleLoginUrl(APIView):
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        """
        If you are building a fullstack application (eq. with React app next to Django)
        you can place this endpoint in your frontend application to receive
        the JWT tokens there - and store them in the state
        """
        client_id = settings.GOOGLE_OAUTH_CLIENT_ID
        techsid = request.GET.get("techsid")
        client_type = request.GET.get('client_type')
        wf_id = request.GET.get('workflow_id') or ""
        state = {
            "wf_id": wf_id,
            "client_type": client_type
        }
        if techsid:
            callback_url = urllib.parse.quote_plus(
                urljoin("https://aidep.cn", reverse("google_callback"))
                + f"?techsid={techsid}"
            )
        else:
            callback_url = urllib.parse.quote_plus(
                urljoin("https://aidep.cn", reverse("google_callback"))
            )
        return Response(
            {
                "status": status.HTTP_200_OK,
                "data": {
                    "url": f"https://accounts.google.com/o/oauth2/v2/auth?redirect_uri={callback_url}&"
                    f"prompt=consent&response_type=code&client_id={client_id}&"
                    f"scope=openid%20email%20profile&access_type=online"
                    f"&state={urllib.parse.quote_plus(urllib.parse.quote_plus(json.dumps(state)))}"
                },
            },
            status=status.HTTP_200_OK,
        )


class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = settings.GOOGLE_OAUTH_CALLBACK_URL
    client_class = OAuth2Client


class GoogleCallback(APIView):
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        code = request.GET.get("code")
        state = request.GET.get("state")
        if code is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        token_endpoint_url = urljoin("https://aidep.cn", reverse("google_login"))
        response = requests.post(
            url=token_endpoint_url, data={"code": code}, timeout=60, verify=False
        )
        res_json = response.json()
        user = res_json.get("user")
        if user:
            # 提交数据到GPU平台换取token，并保存
            if state:
                user = User.objects.get(id=user.get("pk"))
                state = urllib.parse.unquote_plus(state)
                state = json.loads(state)
                techsid = state.get("techsid")
                if techsid:
                    AuthorTechs.objects.create(
                        user=user, techsid=techsid, provider="google"
                    )
                invite = state.get("invite")
                if invite:
                    inviter = InvitationCode.objects.filter(code=invite).first()
                    if inviter:
                        InvitationRelation.objects.create(
                            inviter=inviter.inviter, invitee=user
                        )
                        inviter.accepted = True
                        inviter.save()
                only_login = state.get("only_login")
                if only_login == 1:
                    return redirect(f"https://aidep.cn/#pages/tob/loginSuccess")
                if state.get("client_type"):
                    wf_id = state.get('wf_id')
                    token = res_json.get("access")
                    if state.get('client_type') == 'c':
                        return redirect(f"https://aidep.cn/web/?workflow_id={wf_id}&token={token}")
                    return redirect(f"https://aidep.cn/web-b/?token={token}")
            token = res_json.get("access")
            return redirect(f"https://aidep.cn/web-b/?token={token}")

        token = res_json.get("access")

        return redirect(f"https://aidep.cn/web/?token={token}")


class AccountInfoView(APIView):

    def get(self, request, *args, **kwargs):
        user = request.user
        socialaccount = SocialAccount.objects.filter(user=user).first()
        extra_data = socialaccount.extra_data
        invite_count, flow_count = self.get_extra(user)
        data = {
            "username": extra_data.get("nickname") or extra_data.get("name"),
            "headimgurl": extra_data.get("headimgurl") or extra_data.get("picture"),
            "invite_count": invite_count,
            "flow_count": flow_count
        }
        return Response(
            {"status": status.HTTP_200_OK, "data": data}, status=status.HTTP_200_OK
        )

    def get_extra(self, user):
        from invitation.models import InvitationRelation
        from wxappb.models import AuthorTechs
        from flow.models import WorkFlowData
        invite_count = InvitationRelation.objects.filter(inviter=user).count()
        techs = AuthorTechs.objects.filter(user=user)
        techs = [t.techsid for t in techs]
        flow_count = WorkFlowData.objects.filter(techsid__in=techs).count()
        return invite_count, flow_count


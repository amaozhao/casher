import json
import urllib.parse
from urllib.parse import urljoin

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
from dj_rest_auth.registration.views import SocialLoginView
from wxappb.models import WxAppBTechs


class WXQRCodeAPIView(APIView):
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        # 设置微信扫码登录的 URL，并传入相应的参数
        redirect_uri = urllib.parse.quote_plus(
            urljoin("http://aidep.cn", reverse("weixin_callback"))
        )
        wechat_qr_url = (
            f"https://open.weixin.qq.com/connect/qrconnect?"
            f"appid={settings.SOCIALACCOUNT_PROVIDERS['weixin']['APP']['client_id']}"
            f"&redirect_uri={redirect_uri}"
            f"&response_type=code"
            f"&scope=snsapi_login"
            f"#wechat_redirect"  # 可设置自定义state参数
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


class WXCallback(SocialLoginView):
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        code = request.GET.get("code")
        state = request.GET.get("state")
        if code is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        token_endpoint_url = urljoin("http://aidep.cn", reverse("weixin_login"))
        response = requests.post(
            url=token_endpoint_url, data={"code": code}, timeout=60
        )
        res_json = response.json()
        user = res_json.get("user")
        if user and state:
            user = User.objects.get(id=user.get("pk"))
            state = urllib.parse.unquote_plus(state)
            state = json.loads(state)
            techsid = state.get("techsid")
            WxAppBTechs.objects.create(user=user, techsid=techsid, provider='weixin')
            token = res_json.get("access")
            return redirect(f"http://aidep.cn/web-b/?token={token}")

        token = res_json.get("access")

        return redirect(f"http://aidep.cn/web/?token={token}")


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
        if techsid:
            callback_url = urllib.parse.quote_plus(
                urljoin("http://aidep.cn", reverse("google_callback"))
                + f"?techsid={techsid}"
            )
        else:
            callback_url = urllib.parse.quote_plus(
                urljoin("http://aidep.cn", reverse("google_callback"))
            )
        return Response(
            {
                "status": status.HTTP_200_OK,
                "data": {
                    "url": f"https://accounts.google.com/o/oauth2/v2/auth?redirect_uri={callback_url}&"
                    f"prompt=consent&response_type=code&client_id={client_id}&"
                    f"scope=openid%20email%20profile&access_type=online"
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
        token_endpoint_url = urljoin("http://aidep.cn", reverse("google_login"))
        response = requests.post(
            url=token_endpoint_url, data={"code": code}, timeout=60
        )
        res_json = response.json()
        user = res_json.get("user")
        if user and state:
            user = User.objects.get(id=user.get("pk"))
            state = urllib.parse.unquote_plus(state)
            state = json.loads(state)
            techsid = state.get("techsid")
            WxAppBTechs.objects.create(user=user, techsid=techsid, provider='google')
            token = res_json.get("access")
            return redirect(f"http://aidep.cn/web-b/?token={token}")

        token = res_json.get("access")

        return redirect(f"http://aidep.cn/web/?token={token}")

from urllib.parse import urljoin
import urllib.parse
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.weixin.views import WeixinOAuth2Adapter
import requests
from urllib.parse import urljoin
from django.conf import settings
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class WXQRCodeAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # 设置微信扫码登录的 URL，并传入相应的参数
        redirect_uri = urllib.parse.quote_plus(
            urljoin("http://aidep.cn:8601", reverse("weixin_callback"))
        )
        wechat_qr_url = (
            f"https://open.weixin.qq.com/connect/qrconnect?"
            f"appid={settings.SOCIALACCOUNT_PROVIDERS['weixin']['APP']['client_id']}"
            f"&redirect_uri={redirect_uri}"
            f"&response_type=code"
            f"&scope=snsapi_login"
            f"&state=STATE#wechat_redirect"  # 可设置自定义state参数
        )

        # 直接将微信提供的二维码URL返回给前端
        return Response({"qr_url": wechat_qr_url})


class WXLoginAPIView(APIView):
    adapter_class = WeixinOAuth2Adapter
    callback_url = settings.WEIXIN_OAUTH_CALLBACK_URL
    client_class = OAuth2Client


class WXCallback(APIView):
    def get(self, request, *args, **kwargs):
        # 获取微信返回的授权码
        code = request.GET.get("code")
        if code is None:
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "data": {"error": "Missing code parameter"}
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # 构造微信获取 access_token 的 URL
        token_url = "https://api.weixin.qq.com/sns/oauth2/access_token"
        params = {
            "appid": settings.SOCIALACCOUNT_PROVIDERS["weixin"]["APP"]["client_id"],
            "secret": settings.SOCIALACCOUNT_PROVIDERS["weixin"]["APP"]["secret"],
            "code": code,
            "grant_type": "authorization_code",
        }

        # 请求微信的 access_token 接口
        response = requests.get(token_url, params=params)
        token_data = response.json()

        if "errcode" in token_data:
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "error": "Failed to retrieve access token",
                    "data": token_data
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # 将用户数据返回给前端，或根据需求创建登录逻辑
        return Response(
            {"status": status.HTTP_200_OK, "data": token_data}, status=status.HTTP_200_OK
        )


class GoogleLoginUrl(APIView):
    def get(self, request, *args, **kwargs):
        """
        If you are building a fullstack application (eq. with React app next to Django)
        you can place this endpoint in your frontend application to receive
        the JWT tokens there - and store them in the state
        """
        client_id = settings.GOOGLE_OAUTH_CLIENT_ID
        callback_url = urllib.parse.quote_plus(
            urljoin("http://aidep.cn:8601", reverse("google_callback"))
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

    def get(self, request, *args, **kwargs):
        code = request.GET.get("code")
        if code is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        token_endpoint_url = urljoin("http://aidep.cn:8601", reverse("google_login"))
        response = requests.post(url=token_endpoint_url, data={"code": code})
        return Response(
            {"status": status.HTTP_200_OK, "data": response.json()},
            status=status.HTTP_200_OK,
        )

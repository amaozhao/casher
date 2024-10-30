import urllib.parse
from urllib.parse import urljoin

import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from allauth.socialaccount.adapter import get_adapter
from allauth.socialaccount.helpers import complete_social_login
from allauth.socialaccount.models import SocialAccount, SocialLogin
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.weixin.provider import WeixinProvider
from allauth.socialaccount.providers.weixin.views import WeixinOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework_simplejwt.tokens import RefreshToken


class WXQRCodeAPIView(APIView):
    authentication_classes = []
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
        return Response(
            {"status": status.HTTP_200_OK, "data": {"qr_url": wechat_qr_url}},
            status=status.HTTP_200_OK,
        )


class WXLoginAPIView(APIView):
    adapter_class = WeixinOAuth2Adapter
    callback_url = settings.WEIXIN_OAUTH_CALLBACK_URL
    client_class = OAuth2Client


User = get_user_model()


from allauth.socialaccount.adapter import get_adapter
from allauth.socialaccount.models import SocialAccount, SocialLogin
from allauth.socialaccount.providers.weixin.provider import WeixinProvider
from allauth.socialaccount.providers.weixin.views import WeixinOAuth2Adapter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import get_user_model

User = get_user_model()

class WXCallback(APIView):
    def get(self, request, *args, **kwargs):
        code = request.GET.get("code")
        if code is None:
            return Response({"error": "Missing code parameter"}, status=status.HTTP_400_BAD_REQUEST)

        adapter = WeixinOAuth2Adapter(request)
        token_data = adapter.complete_login(request, code)

        if "error" in token_data:
            return Response({"error": "Failed to retrieve access token"}, status=status.HTTP_400_BAD_REQUEST)

        access_token = token_data.get("access_token")
        openid = token_data.get("openid")

        # 请求微信用户信息
        user_info_url = "https://api.weixin.qq.com/sns/userinfo"
        user_info_response = requests.get(user_info_url, params={
            "access_token": access_token,
            "openid": openid,
            "lang": "zh_CN"
        })
        user_info = user_info_response.json()

        if "errcode" in user_info:
            return Response({"error": "Failed to retrieve user info"}, status=status.HTTP_400_BAD_REQUEST)

        # 检查是否已经存在关联的 SocialAccount
        existing_account = SocialAccount.objects.filter(uid=openid, provider=WeixinProvider.id).first()

        if existing_account:
            social_login = SocialLogin(account=existing_account)
            social_login.user = existing_account.user
        else:
            adapter = get_adapter(request)
            user = adapter.new_user(request)
            user.username = f"wx_{openid}"
            user.set_unusable_password()
            user.save()

            social_account = SocialAccount.objects.create(uid=openid, provider=WeixinProvider.id, user=user)
            social_login = SocialLogin(account=social_account)
            social_login.user = user

        complete_social_login(request, social_login)

        refresh = RefreshToken.for_user(social_login.user)
        return redirect(f"http://aidep.cn:8601/?token={str(refresh.access_token)}")


class GoogleLoginUrl(APIView):
    authentication_classes = None
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
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        code = request.GET.get("code")
        if code is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        token_endpoint_url = urljoin("http://aidep.cn:8601", reverse("google_login"))
        response = requests.post(url=token_endpoint_url, data={"code": code})
        res_json = response.json()
        token = res_json.get("access")

        return redirect(f"http://aidep.cn/?token={token}")

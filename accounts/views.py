from urllib.parse import urljoin
import urllib.parse
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
import requests
from urllib.parse import urljoin
from django.conf import settings
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from allauth.socialaccount.helpers import complete_social_login
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.weixin.provider import WeixinProvider
from allauth.socialaccount.adapter import get_adapter
from allauth.socialaccount.providers.weixin.views import WeixinOAuth2Adapter
from django.contrib.auth import login
from allauth.socialaccount.models import SocialLogin


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
        code = request.GET.get("code")
        if code is None:
            return Response(
                {"error": "Missing code parameter"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Step 1: 通过微信API换取 access_token 和 openid
        token_url = "https://api.weixin.qq.com/sns/oauth2/access_token"
        params = {
            "appid": settings.SOCIALACCOUNT_PROVIDERS["weixin"]["APP"]["client_id"],
            "secret": settings.SOCIALACCOUNT_PROVIDERS["weixin"]["APP"]["secret"],
            "code": code,
            "grant_type": "authorization_code",
        }
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

        access_token = token_data.get("access_token")
        openid = token_data.get("openid")

        # Step 2: 使用allauth创建或关联微信用户
        adapter = WeixinOAuth2Adapter(request)
        adapter.client_id = settings.SOCIALACCOUNT_PROVIDERS["weixin"]["APP"][
            "client_id"
        ]
        adapter.secret = settings.SOCIALACCOUNT_PROVIDERS["weixin"]["APP"]["secret"]

        login_token = adapter.parse_token({"access_token": access_token})
        login_token.token = access_token
        social_login = SocialLogin(
            account=SocialAccount(uid=openid, provider=WeixinProvider.id)
        )
        social_login.token = login_token

        existing_account = SocialAccount.objects.filter(uid=openid, provider=WeixinProvider.id).first()
        if existing_account:
            social_login.user = existing_account.user  # 已存在用户，直接关联
        else:
            user = get_adapter(request).new_user(request, social_login)  # 创建新用户
            user.set_unusable_password()  # 可以设置不可用密码，避免用户直接登录
            user.save()
            social_login.user = user  # 将新用户与 social_login 关联
            social_login.save(request)  # 保存 social_login 记录到数据库

        # 使用 allauth 完成社交登录
        complete_social_login(request, social_login)
        login(request, social_login.user)

        return Response({"status": status.HTTP_200_OK, "user_id": social_login.user.id})

        # 检查是否已存在关联的用户，如果没有则创建
        # try:
        #     existing_account = SocialAccount.objects.filter(uid=openid, provider=WeixinProvider.id).first()
        #     if existing_account:
        #         social_login.user = existing_account.user  # 已存在用户，直接关联
        #     else:
        #         user = get_adapter(request).new_user(request, social_login)  # 创建新用户
        #         user.set_unusable_password()  # 可以设置不可用密码，避免用户直接登录
        #         user.save()
        #         social_login.user = user  # 将新用户与 social_login 关联
        #         social_login.save(request)  # 保存 social_login 记录到数据库
        #
        #     # 使用 allauth 完成社交登录
        #     complete_social_login(request, social_login)
        #     login(request, social_login.user)
        #
        #     return Response({"status": status.HTTP_200_OK, "user_id": social_login.user.id})
        # except Exception as e:
        #     return Response(
        #         {
        #             "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
        #             "error": "Failed to complete social login",
        #             "data": {"details": str(e)}
        #         },
        #         status=status.HTTP_500_INTERNAL_SERVER_ERROR
        #     )


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

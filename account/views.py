from rest_framework.views import APIView
from urllib.parse import urljoin
import urllib.parse

import requests
from django.urls import reverse
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
import json
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView


# class WechatQRLogin(APIView):
#
#     def get(self, request):
#         app = WeChatApp.objects.get_by_name("现金宝H5")
#         url = app.build_url("wechat_callback")
#         cfg = app.configurations
#         redirect = cfg.get("SITE_HOST")
#         client = WeChatOAuthClient(app)
#         url = client.qrconnect_url(redirect_uri=redirect, state="STATE")
#         return Response({"url": url}, status=status.HTTP_200_OK)
#
#
# class WechatMinAppLogin(APIView):
#
#     def post(self, request):
#         app = WeChatApp.objects.get_by_name("现金宝")
#         code = request.data.get("code")
#         user, data = app.auth(code)
#         return Response({"data": data}, status=status.HTTP_200_OK)


# class WechatCallback(APIView):
#     url_name = "wechat_callback"
#
#     def get(self, request):
#         return Response({}, status=status.HTTP_200_OK)


class GoogleLoginUrl(APIView):
    def get(self, request, *args, **kwargs):
        """
        If you are building a fullstack application (eq. with React app next to Django)
        you can place this endpoint in your frontend application to receive
        the JWT tokens there - and store them in the state
        """
        client_id = settings.GOOGLE_OAUTH_CLIENT_ID
        callback_url = urllib.parse.quote_plus(urljoin("http://aidep.cn:8601", reverse("google_login")))
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
        token_endpoint_url = urljoin("http://aidep.cn:8601", reverse("google_login"))
        response = requests.post(url=token_endpoint_url, data={"code": code})
        return Response(response.json(), status=status.HTTP_200_OK)
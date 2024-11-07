import urllib.parse
import json
from urllib.parse import urljoin
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.urls import reverse
from django.conf import settings

from invitation.models import InvitationCode
from allauth.socialaccount.models import SocialAccount


class GetInvitationView(APIView):

    def genarate_weixinb_url(self, code):
        state = {urllib.parse.quote_plus(json.dumps({"invite": code}))}
        redirect_uri = urllib.parse.quote_plus(
            urljoin("https://aidep.cn", reverse("weixin_callback"))
        )
        url = (
            f"https://open.weixin.qq.com/connect/qrconnect?"
            f"appid={settings.WEIXINB_H5_APPID}"
            f"&redirect_uri={redirect_uri}"
            f"&response_type=code"
            f"&scope=snsapi_login"
            f"&state={state}#wechat_redirect"  # 可设置自定义 state 参数
        )
        return url

    def genarate_googleb_url(self, code):
        redirect_uri = urllib.parse.quote_plus(
                urljoin("https://aidep.cn", reverse("google_callback"))
            )
        state = {urllib.parse.quote_plus(json.dumps({"invite": code}))}
        url = (
            f"https://accounts.google.com/o/oauth2/v2/auth?redirect_uri={redirect_uri}&"
            f"prompt=consent&response_type=code&client_id={settings.GOOGLE_OAUTH_CLIENT_ID}&"
            f"scope=openid%20email%20profile&access_type=online&"
            f"state={state}"
        )
        return url

    def get(self, request, *args, **kwargs):
        user = request.user
        social_account = SocialAccount.objects.filter(user=user).first()
        if social_account:
            provider = social_account.get_provider()
        else:
            provider = 'weixin'

        invition = InvitationCode.objects.filter(inviter=user, accepted=False).first()
        if not invition:
            invition = InvitationCode.objects.create(
                inviter=user,
                code=InvitationCode.generate_raw_code()
            )
        if provider == "google":
            invite_url = self.genarate_googleb_url(invition.code)
        else:
            invite_url = self.genarate_weixinb_url(invition.code)
        return Response(
            {
                "data": {
                    "invition": invite_url,
                    "status": status.HTTP_200_OK
                }
            }
        )

from django.conf import settings
from django.shortcuts import redirect
from django.utils.crypto import get_random_string
from rest_framework.views import APIView
import urllib.parse


class GenerateWeixinQRCodeView(APIView):
    def get(self, request, *args, **kwargs):
        app_id = settings.SOCIALACCOUNT_PROVIDERS['weixin']['APP']['client_id']
        redirect_uri = urllib.parse.quote('www.aidep.cn', safe='')
        state = get_random_string(length=32)  # 生成一个32位随机字符串

        qr_code_url = (
            f"https://open.weixin.qq.com/connect/qrconnect?"
            f"appid={app_id}&redirect_uri={redirect_uri}&response_type=code&"
            f"scope=snsapi_login&state={state}"
        )

        return redirect(qr_code_url)

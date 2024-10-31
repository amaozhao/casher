import requests
from django.conf import settings


# 调用微信code2Session接口,换取用户唯一标识 OpenID 和 会话密钥 session_key
def login(code):
    login_url = (
        f"https://api.weixin.qq.com/sns/jscode2session?appid={settings.WEIXIN_APPID}"
        f"&secret={settings.WEIXIN_APPSECRET}&js_code={code}&grant_type=authorization_code"
    )
    response = requests.get(login_url)
    data = response.json()
    print(1111, data)
    if data.get("openid"):
        return data
    else:
        return None

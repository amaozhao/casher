import os

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
    if data.get("openid"):
        return data
    else:
        return None


def get_access_token():
    appid = settings.WEIXIN_APPID
    appsecret = settings.WEIXIN_APPSECRET
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={appsecret}"
    response = requests.get(url)
    data = response.json()
    return data.get("access_token")


def generate_mp_qr_code(path, query, width=430):
    access_token = get_access_token()
    _dir = settings.BASE_DIR / "media/qrcode/c/"
    if not os.path.exists(_dir):
        os.mkdir(_dir)
    # 如果有查询参数，将其添加到路径
    workflow_id = query.get("workflow_id")
    if workflow_id:
        if os.path.exists(settings.BASE_DIR / f"media/qrcode/c/{workflow_id}.png"):
            return f"http://aidep.cn/media/qrcode/c/{workflow_id}.png"
    if query:
        if isinstance(query, dict):
            q = ""
            for k, v in query.items():
                q += f"{k}={v}&"
            path += f"?{query}"
        else:
            path += f"?{query}"

    url = f"https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token={access_token}"
    payload = {"page": "", "scene": "ctest", "width": width, "env_version": "trial"}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        f_name = settings.BASE_DIR / f"media/qrcode/c/{workflow_id}.png"
        with open(f_name, "wb") as f:
            f.write(response.content)
        return f"http://aidep.cn/media/qrcode/c/{workflow_id}.png"
    else:
        return None

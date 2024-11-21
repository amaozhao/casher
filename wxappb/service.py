import os

import requests
from django.conf import settings


# 调用微信code2Session接口,换取用户唯一标识 OpenID 和 会话密钥 session_key
def login(code):
    login_url = (
        f"https://api.weixin.qq.com/sns/jscode2session?appid={settings.WEIXINB_APPID}"
        f"&secret={settings.WEIXINB_APPSECRET}&js_code={code}&grant_type=authorization_code"
    )
    response = requests.get(login_url)
    data = response.json()
    if data.get("openid"):
        return data
    else:
        return None


def get_access_token():
    appid = settings.WEIXINB_APPID
    appsecret = settings.WEIXINB_APPSECRET
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={appsecret}"
    response = requests.get(url)
    data = response.json()
    return data.get("access_token")


def generate_mp_qr_code(query, width=430):
    access_token = get_access_token()
    if not access_token:
        return None  # 没有获取到 access_token，无法生成二维码

    # 获取查询参数
    techsid = query.get("techsid")
    _dir = settings.BASE_DIR / "media/qrcode/b/"
    if not os.path.exists(_dir):
        os.makedirs(_dir)  # 创建完整的目录结构

    # 构建请求 URL 和 Payload
    url = f"https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token={access_token}"
    payload = {
        "page": "",  # 替换为实际页面路径
        "width": width,
        "env_version": "trial",  # 小程序版本：trial=体验版
    }
    if techsid:
        payload["scene"] = techsid[:32]  # 确保scene参数不超过32个字符

    # 生成二维码文件路径
    file_path = settings.BASE_DIR / f"media/qrcode/b/{techsid}.png"
    if not os.path.exists(file_path):  # 如果文件不存在，则生成
        response = requests.post(url, json=payload)
        if response.status_code == 200:  # 如果请求成功
            with open(file_path, "wb") as f:
                f.write(response.content)
        else:
            return None  # 请求失败，返回 None

    # 返回二维码的 URL
    return f"https://aidep.cn/media/qrcode/b/{techsid}.png"

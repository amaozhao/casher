import requests
import json


def get_access_token(appid, secret):
    """
    获取微信小程序的 access_token
    """
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={secret}"
    response = requests.get(url)
    if response.status_code == 200:
        access_token = response.json().get("access_token")
        return access_token
    else:
        raise Exception(f"获取 access_token 失败: {response.text}")


def generate_qrcode(access_token):
    """
    生成微信小程序二维码，并保存到本地
    """
    url = f"https://api.weixin.qq.com/wxa/getwxacode?access_token={access_token}"
    data = {
        "path": path,  # 小程序页面路径
        "width": 430  # 二维码宽度
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"生成二维码失败: {response.text}")


if __name__ == "__main__":
    # 你的小程序的 AppID 和 AppSecret
    appid = "your_appid_here"
    secret = "your_secret_here"

    # 获取 access_token
    access_token = get_access_token(appid, secret)

    # 小程序页面路径
    path = "pages/index/index"

    # 生成二维码
    generate_qrcode(access_token, path)

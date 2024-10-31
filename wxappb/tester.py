import requests


def get_access_token(appid, appsecret):
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={appsecret}"
    response = requests.get(url)
    data = response.json()
    return data.get("access_token")


def generate_mp_qr_code(access_token, path, query=None, width=430):
    # 如果有查询参数，将其添加到路径
    if query:
        path += f"?{query}"

    url = f"https://api.weixin.qq.com/wxa/getwxacode?access_token={access_token}"
    payload = {
        "path": path,
        "width": width,
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        with open("mp_qrcode.png", "wb") as f:
            f.write(response.content)
        print("小程序二维码已生成并保存为 mp_qrcode.png")
    else:
        print("生成二维码失败:", response.json())


if __name__ == "__main__":
    appid = "wx3ade9def38987cbf"
    appsecret = "9970a9332aad6913df0c7291d836bc2e"
    path = "pages/index/index"  # 小程序页面路径

    access_token = get_access_token(appid, appsecret)
    if access_token:
        generate_mp_qr_code(access_token, path)

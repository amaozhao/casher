# views.py
import hashlib
import hmac
import requests
import json

pagsmileAppID = "39CAEFFF1164423EBE9B17FB53597177"
pagsmileappKey = "Lq4Y2Ao7lp"


def generate_authorization_header(app_id, secret_key, payload):
    """
    根据 Pagsmile 的要求，使用 AppId 和 SecretKey 来生成 Authorization 签名。
    """
    # 将 payload 转换为 JSON 格式字符串
    payload_str = json.dumps(payload, separators=(",", ":"))

    # 使用 secret_key 生成 HMAC-SHA256 签名
    signature = hmac.new(
        secret_key.encode(), payload_str.encode(), hashlib.sha256
    ).hexdigest()

    # 返回 Authorization 值（格式为 "AppId:签名"）
    return f"{app_id}:{signature}"


def submit_payout():
    # Pagsmile API endpoint
    url = "https://sandbox.transfersmile.com/api/payout"

    # 请求数据
    payload = {
        "name": "Recipient Name",
        "phone": "1234567890",
        "email": "recipient@example.com",
        "account": "paid@pagsmile.com",
        "account_type": "EMAIL",
        "document_id": "123456789",
        "document_type": "ID",
        "method": "WALLET",
        "channel": "PayPal",
        "custom_code": "your_custom_code",
        "fee_bear": "merchant",
        "amount": "1.00",
        "source_currency": "USD",
        "arrival_currency": "USD",
        "notify_url": "https://your_notify_url.com",
        "additional_remark": "Test payout",
        "country": "USA",
    }

    # 生成 Authorization 头
    headers = {
        "Content-Type": "application/json",
        "AppId": pagsmileAppID,
        "Authorization": generate_authorization_header(
            pagsmileAppID, pagsmileappKey, payload
        ),
    }

    # 发送 POST 请求
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    print(response.text)


if __name__ == "__main__":
    submit_payout()

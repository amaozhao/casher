import hashlib
import json

import requests

pagsmileAppID = "39CAEFFF1164423EBE9B17FB53597177"
pagsmileappKey = "Lq4Y2Ao7lp"


# d is param dict
def ksort(d):
    return [(k, d[k]) for k in sorted(d.keys())]


# sha256
def generate_authorization_header(params, merchantKey):
    params = ksort(params)
    queryStr = ""
    for key, value in params:
        if value:
            queryStr += key + "=" + str(value) + "&"
    h2 = hashlib.sha256()
    h2.update(
        (queryStr.rstrip("&") + merchantKey).encode(encoding="UTF-8", errors="strict")
    )
    return h2.hexdigest()


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
        "method": "WALLET",
        "channel": "PayPal",
        "custom_code": "custom_code123",
        "fee_bear": "merchant",
        "amount": "0.5",
        "source_currency": "USD",
        "arrival_currency": "USD",
        "notify_url": "http://www.deploycloud.cn/api/transactions/callbacks/withdraw",
        "additional_remark": "Test payout",
        "country": "USA",
    }

    # 生成 Authorization 头
    headers = {
        "Content-Type": "application/json",
        "AppId": pagsmileAppID,
        "Authorization": generate_authorization_header(payload, pagsmileappKey),
    }

    # 发送 POST 请求
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    print(response.text)


if __name__ == "__main__":
    submit_payout()

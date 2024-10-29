import hashlib
import json

import requests
from django.conf import settings


class PagsmileService:

    def ksort(self, d):
        return [(k, d[k]) for k in sorted(d.keys())]

    # sha256
    def generate_authorization_header(self, params, merchantKey):
        params = self.ksort(params)
        query_str = ""
        for key, value in params:
            if value:
                query_str += key + "=" + str(value) + "&"
        h2 = hashlib.sha256()
        h2.update(
            (query_str.rstrip("&") + merchantKey).encode(
                encoding="UTF-8", errors="strict"
            )
        )
        return h2.hexdigest()

    def submit_payout(self):
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
            "AppId": settings.PAGSMILE_APP_ID,
            "Authorization": self.generate_authorization_header(
                payload, settings.PAGSMILE_SECRET_KEY
            ),
        }

        # 发送 POST 请求
        response = requests.post(
            settings.PAGSMILE_URL, headers=headers, data=json.dumps(payload)
        )
        return response.json()


pagsmile_service = PagsmileService()

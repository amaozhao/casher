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

    def submit_payout(
        self,
        name,
        phone,
        email,
        account,
        account_type,
        custom_code,
        fee_bear,
        amount,
        source_currency,
        arrival_currency,
        additional_remark,
        country,
    ):

        # 请求数据
        payload = {
            "name": name,
            "phone": phone,
            "email": email,
            "account": account,
            "account_type": account_type,
            "method": "WALLET",
            "channel": "PayPal",
            "custom_code": custom_code,
            "fee_bear": fee_bear or "merchant",
            "amount": str(amount),
            "source_currency": source_currency,
            "arrival_currency": arrival_currency,
            "notify_url": "https://aidep.cn/payment/pagsmile-notify/",
            "additional_remark": additional_remark,
            "country": country,
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

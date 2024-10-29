from django.conf import settings
from random import sample
from string import ascii_letters, digits
import logging
import os
import json
import time
import uuid

from wechatpayv3 import WeChatPay, WeChatPayType


logging.basicConfig(
    filename=os.path.join(os.getcwd(), "wechatpay.log"),
    level=logging.DEBUG,
    filemode="a",
    format="%(asctime)s - %(process)s - %(levelname)s: %(message)s",
)
LOGGER = logging.getLogger("demo")


class WechatPayService:
    def gen_order_number(self):
        return "".join(sample(ascii_letters + digits, 8))

    @property
    def pay_instance(self):
        with open(settings.BASE_DIR / "apiclient_key.pem") as f:
            PRIVATE_KEY = f.read()
        return WeChatPay(
            wechatpay_type=WeChatPayType.NATIVE,
            mchid=settings.WEIXINPAY_MCHID,
            private_key=PRIVATE_KEY,
            cert_serial_no=settings.WEIXINPAY_SERIAL_NO,
            apiv3_key=settings.WEIXINPAY_APIV3KEY,
            appid=settings.WEIXINPAY_APPID,
            notify_url="http://aidep.cn:8601/payment/wechat-notify/",
            cert_dir=None,
            logger=LOGGER,
            partner_mode=False,
            proxy=None,
            timeout=(10, 30),
        )

    def wechatpay(
        self,
        amount,
        desc,
        payer=None,
        payer_client_ip="",
        pay_type=WeChatPayType.MINIPROG,
    ):
        out_trade_no = self.gen_order_number()
        if pay_type == WeChatPayType.JSAPI:
            code, message = self.pay_instance.pay(
                description=desc,
                out_trade_no=out_trade_no,
                amount={"total": amount},
                pay_type=pay_type,
                payer=payer,
            )
            result = json.loads(message)
            if code in range(200, 300):
                prepay_id = result.get("prepay_id")
                timestamp = str(int(time.time()))
                noncestr = str(uuid.uuid4()).replace("-", "")
                package = "prepay_id=" + prepay_id
                sign = self.pay_instance.sign(
                    [settings.WEIXINPAY_APPID, timestamp, noncestr, package]
                )
                signtype = "RSA"
                return {
                    "code": 0,
                    "out_trade_no": out_trade_no,
                    "prepay_id": prepay_id,
                    "result": {
                        "appId": settings.WEIXINPAY_APPID,
                        "timeStamp": timestamp,
                        "nonceStr": noncestr,
                        "package": "prepay_id=%s" % prepay_id,
                        "signType": signtype,
                        "paySign": sign,
                    },
                }
            else:
                return {
                    "out_trade_no": out_trade_no,
                    "code": -1,
                    "result": {"reason": result.get("code")},
                }

        if pay_type == WeChatPayType.H5:
            scene_info = {
                "payer_client_ip": payer_client_ip,
                "h5_info": {"type": "Wap"},
            }
            code, message = self.pay_instance.pay(
                description=desc,
                out_trade_no=out_trade_no,
                amount={"total": amount},
                pay_type=WeChatPayType.H5,
                scene_info=scene_info,
            )
            return {"out_trade_no": out_trade_no, "code": code, "message": message}


wechatpay_service = WechatPayService()

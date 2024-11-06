from django.conf import settings
from yunzhanghu_sdk.client.api.apiusersign_client import ApiUserSignServiceClient
from yunzhanghu_sdk.client.api.model.apiusersign import (
    ApiUserSignRequest,
    GetApiUserSignStatusRequest,
)
from yunzhanghu_sdk.client.api.model.payment import CreateWxpayOrderRequest
from yunzhanghu_sdk.client.api.payment_client import PaymentClient
from yunzhanghu_sdk.config import Config
from yunzhanghu_sdk.message import notify_decoder


class YunAccountService:
    def __init__(self):
        self.config = Config(
            # 生产环境请求域名
            # host = "https://api-service.yunzhanghu.com",
            # 沙箱环境请求域名
            # host = "https://api-service.yunzhanghu.com/sandbox",
            # 个体工商户注册请求域名
            # host = "https://api-aic.yunzhanghu.com",
            # host=settings.YUNZHANGHU_HOST,
            host="https://api-service.yunzhanghu.com/sandbox",
            dealer_id=settings.YUNZHANGHU_DEALER_ID,
            broker_id=settings.YUNZHANGHU_BROKER_ID,
            sign_type="rsa",
            app_key=settings.YUNZHANGHU_APP_KEY,
            des3key=settings.YUNZHANGHU_3DES_KEY,
            dealer_private_key=settings.YUNZHANGHU_PRIVATE_KEY,
            yzh_public_key=settings.YUNZHANGHU_PUBLIC_KEY,
            # 自定义超时时间
            timeout=30,
        )
        self.payment_client = PaymentClient(config=self.config)
        self.sign_client = ApiUserSignServiceClient(config=self.config)

    def user_sign(self, request_id, real_name, id_card, card_type):

        # 用户签约
        req = ApiUserSignRequest(
            dealer_id=self.config.dealer_id,
            broker_id=self.config.broker_id,
            real_name=real_name,
            id_card=id_card,
            card_type=card_type,
        )

        # request-id：请求 ID，请求的唯一标识
        # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
        # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。
        # 注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
        req.request_id = request_id
        try:
            resp = self.sign_client.api_user_sign(req)
            return resp
        except Exception as e:
            # 发生异常
            raise e

    def get_user_sign(self, real_name, id_card):
        # 获取用户签约状态
        req = GetApiUserSignStatusRequest(
            dealer_id=settings.YUNZHANGHU_DEALER_ID,
            broker_id=settings.YUNZHANGHU_BROKER_ID,
            real_name=real_name,
            id_card=id_card,
        )

        # request-id：请求 ID，请求的唯一标识
        # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
        # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。
        # 注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
        req.request_id = "requestIdExample123456789"
        try:
            resp = self.sign_client.get_api_user_sign_status(req)
            return resp
            # if resp.code == "0000":
            #     # 操作成功
            #     return resp
            # else:
            #     # 失败返回
            #     return resp
        except Exception as e:
            # 发生异常
            print(e)

    def wechat_pay_out(
        self,
        request_id,
        order_id,
        real_name,
        openid,
        id_card,
        phone_no,
        pay,
    ):
        req = CreateWxpayOrderRequest(
            order_id=order_id,
            dealer_id=self.config.dealer_id,
            broker_id=self.config.broker_id,
            real_name=real_name,
            openid=openid,
            id_card=id_card,
            phone_no=phone_no,
            pay=pay,
            pay_remark="",
            notify_url="https://aidep.cn/payment/yun_account/notify/",
            wx_app_id="",
            wxpay_mode="transfer",
            project_id="casher",
        )

        # request-id：请求 ID，请求的唯一标识
        # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
        # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。
        # 注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
        req.request_id = request_id
        try:
            resp = self.payment_client.create_wxpay_order(req)
            print(1111, resp)
            return resp
        except Exception as e:
            # 发生异常
            print(e)

    def notify_decode(self, data, mess, timestamp, sign, sign_type):
        verify_result, res_data = notify_decoder(
            settings.YUNZHANGHU_PUBLIC_KEY,
            settings.YUNZHANGHU_APP_KEY,
            settings.YUNZHANGHU_3DES_KEY,
            data,
            mess,
            timestamp,
            sign,
            sign_type,
        )
        return verify_result, res_data


yun_account_service = YunAccountService()

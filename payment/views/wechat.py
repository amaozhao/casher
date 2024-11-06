import uuid

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from payment.models import UserHashrate, WechatOrder, WechatPayout, WechatSign
from payment.services import wechatpay_service, yun_account_service


class CreateWechatPaymentView(APIView):

    def post(self, request, *args, **kwargs):
        user = request.user  # 假设用户已通过身份验证
        request_data = request.data
        amount = request_data.get("amount")
        desc = request_data.get("desc")
        pay_type = request_data.get("pay_type")
        payer = None
        if pay_type == 4:
            payer = {"openid": user.username}
        result = wechatpay_service.wechatpay(
            amount=amount,
            desc=desc or "充值订单",
            payer=payer,
            pay_type=pay_type,
        )
        if result.get("code") == 200:
            WechatOrder.objects.create(
                user=user,
                out_trade_no=result.get("out_trade_no"),
                prepay_id=result.get("prepay_id") or "",
                amount=amount,
                desc=desc,
                pay_type=pay_type,
            )
            return Response(
                {
                    "status": status.HTTP_200_OK,
                    "message": "",
                    "data": {
                        "out_trade_no": result.get("out_trade_no"),
                        "url": result.get("message").get("code_url"),
                    },
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "data": result,
                "message": "error",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


class WechatPayNotifyView(APIView):

    def post(self, request, *args, **kwargs):
        result = wechatpay_service.minip_pay_instance.callback(
            headers=request.META, body=request.body
        )
        if result and result.get("event_type") == "TRANSACTION.SUCCESS":
            resp = result.get("resource")
            out_trade_no = resp.get("out_trade_no")
            amount = resp.get("amount").get("total")
            order = WechatOrder.objects.filter(out_trade_no=out_trade_no).first()
            if order:
                order.status = "succes"
                order.save()
                user = order.user
                hashrate = UserHashrate.objects.filter(user=user).first()
                hashrate.hashrate += amount * 100
                hashrate.save()
            return Response({"code": "SUCCESS", "message": "成功"})
        else:
            return Response(
                {"code": "FAILED", "message": "失败"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class WechatPayCheckView(APIView):
    def get(self, request, *args, **kwargs):
        langStr = request.headers.get("languageStr")
        out_trade_no = request.GET.get("out_trade_no")
        order = WechatOrder.objects.filter(out_trade_no=out_trade_no).first()
        if order:
            return Response(
                {
                    "status": status.HTTP_200_OK,
                    "data": {
                        "out_trade_no": out_trade_no,
                        "trade_status": order.status,
                    },
                }
            )
        message = "支付未完成"
        if langStr == "en-us":
            message = "Payment not completed"
        return Response(
            {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": message,
                "data": {"out_trade_no": out_trade_no, "trade_status": None},
            }
        )


class YunAccountSignView(APIView):
    def post(self, request, *args, **kwargs):
        _sign = WechatSign.objects.filter(user=request.user).first()
        if _sign:
            return Response(
                {"data": {}, "status": status.HTTP_200_OK, "message": "用户已签约"},
                status=status.HTTP_200_OK,
            )
        data = request.data
        real_name = data.get("real_name")
        id_card = data.get("id_card")
        card_type = data.get("card_type")
        phone_no = data.get("phone_no")
        request_id = uuid.uuid4()
        result = yun_account_service.user_sign(
            request_id, real_name, id_card, card_type
        )
        if result.code == "0000":
            WechatSign.objects.create(
                user=self.request.user,
                real_name=real_name,
                id_card=id_card,
                card_type=card_type,
                phone_no=phone_no,
            )
            return Response(
                {"data": result, "status": status.HTTP_200_OK, "message": result.message},
                status=status.HTTP_200_OK,
            )
        if result.code == '5288':
            WechatSign.objects.create(
                user=self.request.user,
                real_name=real_name,
                id_card=id_card,
                card_type=card_type,
                phone_no=phone_no,
            )
        return Response(
            {
                "data": {},
                "status": status.HTTP_400_BAD_REQUEST,
                "message": result.message
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


class YunAccountPayOutView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        wechat_sign = WechatSign.objects.filter(user=request.user).first()
        if not wechat_sign:
            return Response(
                {
                    "data": {"message": "用户未签约, 请先签约再提现"},
                    "status": status.HTTP_400_BAD_REQUEST,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        request_id = str(uuid.uuid4())
        pay = data.get("fee")
        order_id = str(uuid.uuid4())
        openid = str(uuid.uuid4())
        result = yun_account_service.wechat_pay_out(
            request_id,
            order_id,
            wechat_sign.real_name,
            openid,
            wechat_sign.id_card,
            wechat_sign.phone_no,
            pay,
        )
        if result.code == "0000":
            WechatPayout.objects.create(
                user=self.request.user,
                order_id=order_id,
                request_id=request_id,
                open_id=openid,
                real_name=wechat_sign.real_name,
                id_card=wechat_sign.id_card,
                # card_type=wechat_sign.id_type,
                phone_no=wechat_sign.phone_no,
                pay=pay,
            )
            return Response(
                {"data": result.data, "status": status.HTTP_200_OK},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"data": {}, "status": status.HTTP_500_INTERNAL_SERVER_ERROR},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


class YunAccountNotifyView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.POST.get("data")
        mess = request.POST.get("mess")
        timestamp = int(request.POST.get("timestamp"))
        sign = request.POST.get("sign")
        sign_type = request.POST.get("sign_type")
        # 验证签名+解密
        verify_result, res_data = yun_account_service.notify_decode(
            data, mess, timestamp, sign, sign_type
        )
        if verify_result:
            # 业务逻辑处理
            request_id = res_data.get("request_id")
            pay_out = WechatPayout.objects.filter(request_id=request_id).first()
            if pay_out:
                pay_out.status = "success"
                pay_out.save()
                return Response(
                    {
                        "data": {"message": "success"},
                    },
                    status=status.HTTP_200_OK,
                )
            return Response(
                {
                    "data": {"message": "fail"},
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

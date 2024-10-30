from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from payment.models import UserHashrate, WechatOrder
from payment.services import wechatpay_service


class CreateWechatPaymentView(APIView):

    def post(self, request, *args, **kwargs):
        user = request.user  # 假设用户已通过身份验证
        request_data = request.data
        amount = request_data.get("amount")
        desc = request_data.get("desc")
        pay_type = request_data.get("pay_type")
        payer_client_ip = request.META.get("HTTP_X_FORWARDED_FOR")
        payer = None
        if pay_type == 0:
            payer = {"openid": "get_openid"}
        result = wechatpay_service.wechatpay(
            amount=amount,
            desc=desc,
            payer=payer,
            payer_client_ip=payer_client_ip,
            pay_type=pay_type,
        )
        if result.get("code") == 0:
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
                    "data": result
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "data": result,
                "message": "error"
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


class WechatPayNotifyView(APIView):

    def post(self, request, *args, **kwargs):
        result = wechatpay_service.pay_instance.callback(
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

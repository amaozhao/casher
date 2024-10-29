from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from payment.models import UserHashrate
from payment.services import wechatpay_service


class CurrentUserHashrateView(APIView):

    def get(self, request, *args, **kwargs):
        user = request.user  # 假设用户已通过身份验证
        hastrate = UserHashrate.objects.filter(user=user).first()
        if not hastrate:
            hastrate = UserHashrate.objects.create(user=user, hashrate=0)
        return Response(
            {"status": status.HTTP_200_OK, "data": {"account": hastrate.hashrate}}
        )


class HashrateTemplateView(APIView):

    def get(self, request, *args, **kwargs):
        return Response(
            {
                "status": status.HTTP_200_OK,
                "data": {
                    "PowerPurchaseOptions": [
                        {
                            "ID": 1,
                            "AmountInCurrency": 1,
                            "PowerAmount": 100,
                            "DiscountRate": 1,
                            "IsActive": True,
                        },
                        {
                            "ID": 2,
                            "AmountInCurrency": 2,
                            "PowerAmount": 200,
                            "DiscountRate": 1,
                            "IsActive": True,
                        },
                        {
                            "ID": 3,
                            "AmountInCurrency": 5,
                            "PowerAmount": 500,
                            "DiscountRate": 1,
                            "IsActive": True,
                        },
                        {
                            "ID": 4,
                            "AmountInCurrency": 10,
                            "PowerAmount": 1000,
                            "DiscountRate": 1,
                            "IsActive": True,
                        },
                    ]
                },
                "message": "操作成功",
            },
            status=status.HTTP_200_OK,
        )


class HashrateconvertView(APIView):
    def post(self, request, *args, **kwargs):
        amount = request.data.get("amount")
        return Response(
            {"status": status.HTTP_200_OK, "data": {"currency": round(amount / 100, 2)}}
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

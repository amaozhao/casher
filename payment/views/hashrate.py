from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from payment.models import UserHashrate


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
            {"status": status.HTTP_200_OK, "data": {"currency": round(amount / 100, 2), "message": ""}}
        )

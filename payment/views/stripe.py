from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class CreatePaymentIntentView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # 从请求数据中获取金额和货币信息
            amount = request.data.get('amount')
            currency = request.data.get('currency', 'usd')

            # 创建Payment Intent
            intent = stripe.PaymentIntent.create(
                amount=int(amount),  # 以分为单位
                currency=currency,
                payment_method_types=["card"],  # 支持的支付方式
            )

            # 返回客户端需要的client_secret
            return Response({"client_secret": intent.client_secret}, status=status.HTTP_201_CREATED)
        except stripe.error.StripeError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

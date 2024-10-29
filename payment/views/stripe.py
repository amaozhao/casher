import stripe
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from payment.utils import get_or_create_stripe_customer

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class CreatePaymentIntentView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user  # 假设用户已通过身份验证

        try:
            # 获取或创建用户的Stripe客户ID
            stripe_customer_id = get_or_create_stripe_customer(user)

            # 从请求数据中获取金额和货币信息
            amount = request.data.get("amount")
            currency = request.data.get("currency", "usd")

            # 创建Payment Intent并关联客户
            intent = stripe.PaymentIntent.create(
                amount=int(amount),
                currency=currency,
                customer=stripe_customer_id,  # 关联Stripe客户
                payment_method_types=["card"],
            )

            return Response(
                {
                    'status': status.HTTP_201_CREATED,
                    'data': {"client_secret": intent.client_secret}
                },
                status=status.HTTP_201_CREATED
            )
        except stripe.error.StripeError as e:
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "data": {"error": str(e)}
                }, status=status.HTTP_400_BAD_REQUEST)

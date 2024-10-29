import stripe
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from payment.utils import get_or_create_stripe_customer

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class CreateCheckoutView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user  # 假设用户已通过身份验证

        try:
            # 从请求数据中获取金额和货币信息
            amount = request.data.get("amount")
            currency = request.data.get("currency", "usd")
            current_url = request.data.get("current_url")

            checkout_session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[
                    {
                        "price_data": {
                            "currency": currency,
                            "product_data": {
                                "name": "Hashrate charge",
                            },
                            "unit_amount": int(int(amount) / 10),  # 以分为单位
                        },
                        "quantity": 1,
                    }
                ],
                mode="payment",
                success_url=current_url,
                cancel_url=current_url,
            )

            return Response(
                {"status": status.HTTP_200_OK, "data": {"url": checkout_session.url}},
                status=status.HTTP_200_OK,
            )
        except stripe.error.StripeError as e:
            return Response(
                {"status": status.HTTP_400_BAD_REQUEST, "data": {"error": str(e)}},
                status=status.HTTP_400_BAD_REQUEST,
            )

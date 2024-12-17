import stripe
from django.conf import settings
from djstripe.models import Customer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from djstripe.models import PaymentMethod

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class StripBindView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # 从请求数据中获取金额和货币信息
            current_url = request.data.get("current_url")
            # metadata = {"user_id": self.request.user.id}

            customer, created = Customer.get_or_create(subscriber=self.request.user)

            checkout_session = stripe.checkout.Session.create(
                customer=customer.id,
                payment_method_types=["card"],
                mode="setup",
                success_url=current_url,
                cancel_url=current_url,
                # metadata=metadata,
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

    def get(self, request, *args, **kwargs):
        user = request.user
        customer = user.customer  # 假设用户模型和 Customer 关联
        payment_method = PaymentMethod.objects.filter(customer=customer.id).first()
        if payment_method:
            return Response(
                {"status": status.HTTP_200_OK, "data": {"bind_status": True}},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"status": status.HTTP_400_BAD_REQUEST, "data": {"bind_status": False}},
            status=status.HTTP_400_BAD_REQUEST,
        )

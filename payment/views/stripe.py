import stripe
from django.conf import settings
from djstripe.models import Customer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class CreateCheckoutView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # 从请求数据中获取金额和货币信息
            current_url = request.data.get("current_url")
            metadata = {"user_id": self.request.user.id}

            customer = Customer.objects.get(subscriber=self.request.user)

            checkout_session = stripe.checkout.Session.create(
                customer=customer.id,
                payment_method_types=["card"],
                mode="setup",
                success_url=current_url,
                cancel_url=current_url,
                metadata=metadata,
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


class BindPaymentMethodView(APIView):
    """
    绑定信用卡视图
    """

    def post(self, request, *args, **kwargs):
        user = request.user  # 假设用户已登录
        payment_method_id = request.POST.get("payment_method_id")
        languagestr = self.request.headers.get("languagestr")

        if not payment_method_id:
            msg = "缺少 payment_method_id"
            if languagestr == 'en':
                msg = 'payment_method_id is missing'
            return Response(
                {
                    "data": {
                        "message": msg
                    },
                    "status": status.HTTP_400_BAD_REQUEST
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # 获取或创建 Stripe Customer
            customer, created = Customer.get_or_create(subscriber=user)

            # 绑定 PaymentMethod 到 Customer
            stripe.PaymentMethod.attach(
                payment_method_id,
                customer=customer.id,
            )

            # 设置默认支付方式
            stripe.Customer.modify(
                customer.id,
                invoice_settings={"default_payment_method": payment_method_id},
            )

            msg = "信用卡绑定成功！"
            if languagestr == 'en':
                msg = 'Credit card binding successful!'
            return Response(
                {
                    "data": {
                        "message": "msg"
                    },
                    "status": status.HTTP_200_OK
                }
            )
        except stripe.error.StripeError as e:
            return Response(
                {
                    {
                        "data": {
                            "message": str(e)
                        },
                        "status": status.HTTP_400_BAD_REQUEST
                    }
                },
                status=400
            )

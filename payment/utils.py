import stripe
from django.conf import settings
from payment.models import PaymentProfile

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


def get_or_create_stripe_customer(user):
    payment_profile = PaymentProfile.objects.filter(user=user).first()
    if not payment_profile:
        payment_profile = PaymentProfile.objects.create(user=user)
        customer = stripe.Customer.create(email=user.email)
        payment_profile.stripe_customer_id = customer.id
        payment_profile.save()
        return customer.id
    if payment_profile.stripe_customer_id:
        # 用户已经有了Stripe客户ID
        return payment_profile.stripe_customer_id
    else:
        # 创建新的Stripe客户
        customer = stripe.Customer.create(email=user.email)
        payment_profile.stripe_customer_id = customer.id
        payment_profile.save()
        return customer.id

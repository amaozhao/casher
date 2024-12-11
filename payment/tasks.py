import stripe
from djstripe.models import Customer
from .models import StripeBill
from django.utils import timezone
from celery import shared_task
from datetime import timedelta


@shared_task
def process_weekly_billing():
    now = timezone.now()
    start_of_last_week = now - timedelta(days=now.weekday() + 7)  # 获取上周一
    end_of_last_week = start_of_last_week + timedelta(days=6)  # 获取上周日

    # 查询上周未支付的账单
    bills = StripeBill.objects.filter(
        created_at__gte=start_of_last_week,
        created_at__lte=end_of_last_week,
        paid=False
    )

    users_to_charge = set(bill.user for bill in bills)

    for user in users_to_charge:
        user_bills = bills.filter(user=user)
        total_amount = sum(bill.amount for bill in user_bills)

        try:
            # 获取用户的 Stripe 客户信息
            customer = Customer.objects.get(subscriber=user)
            # 使用默认支付方式自动扣费
            payment_intent = stripe.PaymentIntent.create(
                amount=int(total_amount * 100),  # 金额以分为单位
                currency="usd",
                customer=customer.id,
                payment_method=customer.default_payment_method.id,
                off_session=True,  # 用户不在线
                confirm=True,      # 自动确认支付
                description=f"Weekly billing for {user.username}",
            )

            # 如果扣费成功，标记账单为已支付
            if payment_intent.status == "succeeded":
                # user_bills.update(paid=True)
                print(f"Successfully charged {user} for {total_amount}")
            else:
                print(f"Payment failed for {user} - PaymentIntent status: {payment_intent.status}")

        except stripe.error.CardError as e:
            # 如果支付失败，可以记录日志或通知管理员
            print(f"Failed to charge {user}: {e.user_message}")

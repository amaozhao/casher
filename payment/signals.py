from django.db.models.signals import post_save
from django.dispatch import receiver
from djstripe.models import Event
from payment.models import UserHashrate
from payment.models import PaymentProfile


@receiver(post_save, sender=Event)
def my_custom_event_handler(sender, instance, created, **kwargs):
    # 确保仅处理新创建的事件
    if created:
        if instance.event_type == "payment_intent.succeeded":
            # 添加您的自定义逻辑
            customer = instance.customer
            profile = PaymentProfile.objects.filter(stripe_customer_id=customer.id).first()
            payment_intent = instance.data.get("object")
            amount = payment_intent.get("amount")
            update_user_hashrate(profile.user, amount)
            print("Custom logic for payment_intent.succeeded")
            # 您的处理代码，例如更新订单状态


def update_user_hashrate(user, amount):
    user_hashrate = UserHashrate.objects.filter(user=user).first()
    if not user_hashrate:
        user_hashrate = UserHashrate.objects.create(
            user = user,
            hashrate=0.0
        )
    init_rate = user_hashrate.hashrate
    init_rate += amount * 1000
    user_hashrate.hashrate = init_rate
    user_hashrate.save()

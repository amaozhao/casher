from djstripe.event_handlers import djstripe_receiver
from djstripe.models import Event, PaymentMethod
from django.utils import timezone
from datetime import timedelta

from payment.models import StripeBill


@djstripe_receiver("checkout.session.completed")
def handle_charge_succeeded(sender, **kwargs):
    event: Event = kwargs.get("event")
    session = event.data["object"]
    customer_id = session["customer"]
    payment_method_id = session["setup_intent"]
    from djstripe.models import Customer
    customer = Customer.objects.get(id=customer_id)
    user = customer.subscriber

    # 自定义绑定支付方式逻辑
    bind_payment_method(user, payment_method_id)


def bind_payment_method(user, payment_method_id):
    """
    自定义绑定支付方式逻辑
    """
    customer = user.customer  # 假设用户模型和 Customer 关联
    payment_method = PaymentMethod.attach(payment_method_id, customer=customer.id)
    customer.default_payment_method = payment_method
    customer.save()
    return customer


@djstripe_receiver("invoice.payment_failed")
def invoice_payment_failed(sender, **kwargs):
    event: Event = kwargs.get("event")
    invoice_data = event.data['object']  # 获取 invoice 对象
    invoice_id = invoice_data['id']
    pass


@djstripe_receiver("payment_intent.succeeded")
def handle_payment_intent_succeeded(sender, **kwargs):
    event: Event = kwargs.get("event")
    session = event.data["object"]
    customer_id = session["customer"]
    now = timezone.now()
    start_of_last_week = now - timedelta(days=now.weekday() + 7)  # 获取上周一
    end_of_last_week = start_of_last_week + timedelta(days=6)  # 获取上周日
    from djstripe.models import Customer
    customer = Customer.objects.get(id=customer_id)
    user = customer.subscriber
    StripeBill.objects.filter(
        user__id=user.id,
        created_at__gte=start_of_last_week,
        created_at__lte=end_of_last_week,
        paid=False
    ).update(paid=True)

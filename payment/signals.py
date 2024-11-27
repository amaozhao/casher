from djstripe.event_handlers import djstripe_receiver
from djstripe.models import Event, Charge, PaymentMethod
import stripe

from payment.models import StripePaymentProfile, UserHashrate


def update_user_hashrate(user, amount):
    user_hashrate = UserHashrate.objects.filter(user=user).first()
    if not user_hashrate:
        user_hashrate = UserHashrate.objects.create(user=user, hashrate=0)
    init_rate = user_hashrate.hashrate
    init_rate += amount * 100
    user_hashrate.hashrate = init_rate
    user_hashrate.save()


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
    stripe.PaymentMethod.attach(
        payment_method_id,
        customer=customer.id,
    )
    stripe.Customer.modify(
        customer.id,
        invoice_settings={"default_payment_method": payment_method_id},
    )
    print(f"绑定支付方式成功: {payment_method_id}")


@djstripe_receiver("invoice.payment_succeeded")
def handle_payment_method_attached(sender, **kwargs):
    event: Event = kwargs.get("event")
    customer_id = event.data["object"]["customer"]
    print("Payment Method Attached!")
    print(f"Sender: {sender}")
    print(f"Event: {event}")

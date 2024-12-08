from djstripe.event_handlers import djstripe_receiver
from djstripe.models import Event, Invoice
import stripe

from payment.models import UserHashrate


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


@djstripe_receiver("invoice.payment_failed")
def invoice_payment_failed(sender, **kwargs):
    event: Event = kwargs.get("event")
    invoice_data = event.data['object']  # 获取 invoice 对象
    invoice_id = invoice_data['id']
    pass

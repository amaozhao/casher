from djstripe.event_handlers import djstripe_receiver
from djstripe.models import Event, PaymentMethod

from payment.models import UserHashrate


@djstripe_receiver("checkout.session.async_payment_succeeded")
def handle_checkout_succeeded(sender, **kwargs):
    event: Event = kwargs.get("event")
    amount_total = event.data["object"]["amount_total"]
    hashrate = int(amount_total * 7.1 * 1000)
    # currency = event.data['object']['currency']
    user_id = event.data["object"]["metadata"].get("user_id")
    user_hashrate = UserHashrate.objects.get_or_create(user_id=user_id)
    user_hashrate.hashrate += hashrate
    user_hashrate.save()


@djstripe_receiver("checkout.session.async_payment_failed")
def handle_payment_method_attached(sender, **kwargs):
    event: Event = kwargs.get("event")
    payment_method_id = event.data["object"]["id"]
    payment_method = PaymentMethod.objects.get(id=payment_method_id)
    print("Payment Method Attached!")
    print(f"Sender: {sender}")
    print(f"Event: {event}")
    print(f"Payment Method: {payment_method}")

from django.urls import path
from payment.views import CreatePaymentIntentView, CreatePayoutView

urlpatterns = [
    path('create-payment/', CreatePaymentIntentView.as_view(), name='create_payment_intent'),
    path("create-payout/", CreatePayoutView.as_view(), name="create_payout"),
]
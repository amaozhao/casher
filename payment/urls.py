from django.urls import path
from payment.views import CreatePaymentIntentView

urlpatterns = [
    path('create-payment/', CreatePaymentIntentView.as_view(), name='create-payment-intent'),
]
from django.urls import path

from payment.views import (
    CreatePaymentIntentView,
    CreateWechatPaymentView,
    WechatPayNotifyView,
)

urlpatterns = [
    path(
        "create-payment/",
        CreatePaymentIntentView.as_view(),
        name="create_payment_intent",
    ),
    # path("create-payout/", CreatePayoutView.as_view(), name="create_payout"),
    path(
        "create-wechatpay/",
        CreateWechatPaymentView.as_view(),
        name="create_wechatpay",
    ),
    path(
        "wechat-notify/",
        WechatPayNotifyView.as_view(),
        name="wechat_notify",
    ),
]

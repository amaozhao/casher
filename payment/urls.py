from django.urls import path

from payment.views import (
    CreatePaymentIntentView,
    CreateWechatPaymentView,
    WechatPayNotifyView,
    PagsmileNotify,
    PagsmilePayoutView
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
    path(
        "create-pagsmile-payout/",
        PagsmilePayoutView.as_view(),
        name="pagsmile_payout",
    ),
    path(
        "pagsmile-notify/",
        PagsmileNotify.as_view(),
        name="pagsmile_notify",
    ),
]

from django.urls import path

from payment.views import (
    CreateCheckoutView,
    CreateWechatPaymentView,
    CurrentUserHashrateView,
    HashrateconvertView,
    HashrateTemplateView,
    PagsmileNotify,
    PagsmilePayoutView,
    WechatPayNotifyView,
)

urlpatterns = [
    path(
        "create-payment/",
        CreateCheckoutView.as_view(),
        name="create_checkout_paymentt",
    ),
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
    path(
        "user-hashrate/",
        CurrentUserHashrateView.as_view(),
        name="hashrate_user",
    ),
    path(
        "hashrate-template/",
        HashrateTemplateView.as_view(),
        name="hashrate_template",
    ),
    path(
        "hashrate-convert/",
        HashrateconvertView.as_view(),
        name="hashrate_convert",
    ),
]

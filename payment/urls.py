from django.urls import path

from payment.views import (
    CashInListView,
    CashOutListView,
    CreateCheckoutView,
    CreateWechatPaymentView,
    CurrentUserHashrateView,
    HashrateconvertView,
    HashrateTemplateView,
    PagsmileNotify,
    PagsmilePayoutView,
    WechatPayCheckView,
    WechatMiniPayNotifyView,
    WechatPayNotifyView,
    YunAccountNotifyView,
    YunAccountPayOutView,
    YunAccountSignView,
    BindPaymentMethodView,
)

urlpatterns = [
    path(
        "cashout/",
        CashOutListView.as_view(),
        name="cashout",
    ),
    path(
        "cashin/",
        CashInListView.as_view(),
        name="cashin",
    ),
    path(
        "stripe-bind/",
        BindPaymentMethodView.as_view(),
        name="stripe_bind",
    ),
    path(
        "create-payment/",
        CreateCheckoutView.as_view(),
        name="create_checkout_payment",
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
        "wechat-mini-notify/",
        WechatMiniPayNotifyView.as_view(),
        name="wechat_notify",
    ),
    path("yun_account/sign/", YunAccountSignView.as_view(), name="yunaccount-sign"),
    path(
        "yun_account/payout/", YunAccountPayOutView.as_view(), name="yunaccount-payout"
    ),
    path(
        "yun_account/notify/", YunAccountNotifyView.as_view(), name="yunaccount-notify"
    ),
    path(
        "wechat-check/",
        WechatPayCheckView.as_view(),
        name="wechat_check",
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

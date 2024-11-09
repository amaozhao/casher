from django.conf import settings
from django.db import models

from flow.models import WorkFlowData


class StripePaymentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "payment_profile"


class PagsmilePayout(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=20, default="")
    email = models.CharField(max_length=20, default="")
    account = models.CharField(max_length=20, default="")
    account_type = models.CharField(max_length=20, default="")
    method = models.CharField(max_length=20, default="WALLET")
    channel = models.CharField(max_length=20, default="PayPal")
    custom_code = models.CharField(max_length=20)
    fee_bear = models.CharField(max_length=20, default="merchant")
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    source_currency = models.CharField(max_length=20, default="USD")
    arrival_currency = models.CharField(max_length=20, default="USD")
    notify_url = models.CharField(
        max_length=20, default="https://aidep.cn/payment/pagsmile/callback/"
    )
    additional_remark = models.TextField(default="")
    country = models.CharField(max_length=20, default="USA")
    status = models.CharField(max_length=20, default="prepayout")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "pagsmile_payout"
        indexes = [
            models.Index(
                fields=[
                    "custom_code",
                ],
                name="custom_code_idx",
            ),
        ]


class UserHashrate(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hashrate = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_hashrate"


class WechatOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    out_trade_no = models.CharField(max_length=100)
    prepay_id = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    desc = models.TextField(default="")
    pay_type = models.IntegerField()
    status = models.CharField(max_length=100, default="prepay")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "wechat_order"


class WechatSign(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    real_name = models.CharField(max_length=100)
    id_card = models.CharField(max_length=100)
    id_type = models.CharField(max_length=40)
    phone_no = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "wechat_sign"


class WechatPayout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    request_id = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100)
    real_name = models.CharField(max_length=100)
    open_id = models.CharField(max_length=100)
    id_card = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    pay = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default="init")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "wechat_payout"


class UserPayin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    workflow = models.ForeignKey(WorkFlowData, on_delete=models.CASCADE)
    fee = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    currency = models.CharField(max_length=20, default="CNY")
    pay_type = models.CharField(max_length=100, default="author")
    status = models.CharField(max_length=100, default="success")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_payin"

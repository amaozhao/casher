from django.conf import settings
from django.db import models


class PaymentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "payment_profile"


class UserHashrate(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hashrate = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)

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

    class Meta:
        db_table = "wechat_order"

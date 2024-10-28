from django.conf import settings
from django.db import models


class PaymentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=255, blank=True, null=True)


class UserHashrate(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hashrate = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)

from django.db import models
from django.contrib.auth.models import User


class CommissionConfig(models.Model):
    author_take = models.FloatField(default=0.7)
    invitation_take = models.FloatField(default=0.1)
    platform_take = models.FloatField(default=0.2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "commission_config"
        ordering = ["-updated"]


class CashStatistics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cashable = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)         # 可提现
    withdrawing = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)      # 提现中
    withdrawned = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)      # 已提现
    total_income = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)     # 总收入
    in_transit = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)       # 在途
    refunded = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)         # 已退款
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "cash_statistics"
        ordering = ["-updated"]

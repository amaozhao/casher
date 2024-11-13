from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class GPUAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    unique_target = models.CharField(max_length=100)
    token = models.CharField(max_length=1024)
    expired = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "gpu_account"

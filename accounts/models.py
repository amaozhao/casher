from django.db import models
from django.contrib.auth.models import User


class OfficialAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_official = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "official_account"
        ordering = ["-updated"]


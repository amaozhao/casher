from django.contrib.auth.models import User
from django.db import models


class WxAppBUserProfile(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.deletion.CASCADE,
    )
    nick_name = models.CharField(max_length=255, default="")
    gender = models.IntegerField(default=0)
    city = models.CharField(max_length=100, default="")
    province = models.CharField(max_length=100, default="")
    country = models.CharField(max_length=100, default="")
    avatarUrl = models.CharField(max_length=500, default="")
    unionid = models.CharField(max_length=500, default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "wxappb_user_profile"
        ordering = ["-created"]


class WxAppBTechs(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.deletion.CASCADE,
    )
    techsid = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "wxappb_tesh"
        ordering = ["-created"]

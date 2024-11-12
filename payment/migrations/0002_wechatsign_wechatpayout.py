# Generated by Django 4.2.16 on 2024-11-06 06:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("payment", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="WechatSign",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("real_name", models.CharField(max_length=100)),
                ("id_card", models.CharField(max_length=100)),
                ("id_type", models.CharField(max_length=40)),
                ("phone_no", models.CharField(max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "wechat_sign",
            },
        ),
        migrations.CreateModel(
            name="WechatPayout",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("request_id", models.CharField(max_length=100)),
                ("order_id", models.CharField(max_length=100)),
                ("real_name", models.CharField(max_length=100)),
                ("open_id", models.CharField(max_length=100)),
                ("id_card", models.CharField(max_length=100)),
                ("phone_no", models.CharField(max_length=100)),
                ("pay", models.CharField(max_length=100)),
                ("status", models.CharField(default="init", max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "wechat_payout",
            },
        ),
    ]

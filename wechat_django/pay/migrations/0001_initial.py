# Generated by Django 4.2.16 on 2024-10-22 03:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import wechat_django.pay.models.base


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wechat_django", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UnifiedOrder",
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
                (
                    "device_info",
                    models.CharField(
                        max_length=32, null=True, verbose_name="device_info"
                    ),
                ),
                ("body", models.CharField(max_length=128, verbose_name="order body")),
                (
                    "detail",
                    models.TextField(
                        max_length=6000, null=True, verbose_name="order detail"
                    ),
                ),
                (
                    "out_trade_no",
                    models.CharField(max_length=32, verbose_name="out_trade_no"),
                ),
                (
                    "fee_type",
                    models.CharField(
                        default="CNY", max_length=16, null=True, verbose_name="fee_type"
                    ),
                ),
                ("total_fee", models.PositiveIntegerField(verbose_name="total_fee")),
                (
                    "spbill_create_ip",
                    models.CharField(max_length=64, verbose_name="spbill_create_ip"),
                ),
                (
                    "time_start",
                    wechat_django.pay.models.base.PayDateTimeField(
                        default=django.utils.timezone.now, verbose_name="time_start"
                    ),
                ),
                (
                    "time_expire",
                    wechat_django.pay.models.base.PayDateTimeField(
                        verbose_name="time_expire"
                    ),
                ),
                (
                    "goods_tag",
                    models.CharField(
                        max_length=32, null=True, verbose_name="goods_tag"
                    ),
                ),
                (
                    "trade_type",
                    models.CharField(
                        choices=[
                            ("APP", "APP"),
                            ("JSAPI", "JSAPI"),
                            ("MICROPAY", "MICROPAY"),
                            ("MWEB", "MWEB"),
                            ("NATIVE", "NATIVE"),
                        ],
                        max_length=16,
                        verbose_name="trade_type",
                    ),
                ),
                (
                    "product_id",
                    models.CharField(
                        max_length=32, null=True, verbose_name="product id"
                    ),
                ),
                (
                    "limit_pay",
                    models.CharField(
                        choices=[("no_credit", "NOCREDIT"), (None, "NONE")],
                        default=None,
                        max_length=32,
                        null=True,
                        verbose_name="limit_pay",
                    ),
                ),
                (
                    "openid",
                    models.CharField(max_length=128, null=True, verbose_name="openid"),
                ),
                (
                    "sub_openid",
                    models.CharField(
                        max_length=128, null=True, verbose_name="sub openid"
                    ),
                ),
                (
                    "receipt",
                    models.CharField(
                        choices=[(None, "NONE"), ("Y", "TRUE")],
                        default=None,
                        max_length=8,
                        null=True,
                        verbose_name="recept",
                    ),
                ),
                (
                    "scene_info",
                    models.JSONField(
                        max_length=256, null=True, verbose_name="scene_info"
                    ),
                ),
                ("comment", models.TextField(blank=True, verbose_name="comment")),
                ("ext_info", models.JSONField(default=dict, editable=False)),
                (
                    "_call_args",
                    models.JSONField(
                        db_column="call_args", default=dict, editable=False, null=True
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="updated at"),
                ),
            ],
            options={
                "verbose_name": "Unified order",
                "verbose_name_plural": "Unified orders",
            },
        ),
        migrations.CreateModel(
            name="WeChatPay",
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
                (
                    "title",
                    models.CharField(
                        blank=True,
                        help_text="商户号标识,用于后台辨识商户号",
                        max_length=16,
                        verbose_name="title",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        default="default",
                        help_text="商户号程序标识",
                        max_length=16,
                        verbose_name="name",
                    ),
                ),
                ("weight", models.IntegerField(default=0, verbose_name="weight")),
                (
                    "mch_id",
                    models.CharField(
                        help_text="微信支付分配的商户号",
                        max_length=32,
                        verbose_name="mch_id",
                    ),
                ),
                (
                    "api_key",
                    models.CharField(
                        help_text="商户号key",
                        max_length=128,
                        verbose_name="WeChatPay api_key",
                    ),
                ),
                (
                    "sub_mch_id",
                    models.CharField(
                        blank=True,
                        help_text="子商户号，受理模式下填写",
                        max_length=32,
                        null=True,
                        verbose_name="sub_mch_id",
                    ),
                ),
                (
                    "mch_app_id",
                    models.CharField(
                        blank=True,
                        help_text="微信分配的主商户号appid，受理模式下填写",
                        max_length=32,
                        null=True,
                        verbose_name="mch_app_id",
                    ),
                ),
                (
                    "mch_cert",
                    models.BinaryField(blank=True, null=True, verbose_name="mch_cert"),
                ),
                (
                    "mch_key",
                    models.BinaryField(blank=True, null=True, verbose_name="mch_key"),
                ),
                (
                    "app",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pays",
                        to="wechat_django.wechatapp",
                    ),
                ),
            ],
            options={
                "verbose_name": "WeChat pay",
                "verbose_name_plural": "WeChat pay",
                "ordering": ("app", "-weight", "pk"),
                "unique_together": {("app", "name")},
            },
        ),
        migrations.CreateModel(
            name="UnifiedOrderResult",
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
                (
                    "transaction_id",
                    models.CharField(
                        max_length=32, null=True, verbose_name="transaction_id"
                    ),
                ),
                (
                    "trade_state",
                    models.CharField(
                        choices=[
                            ("CLOSED", "CLOSED"),
                            ("FAIL", "FAIL"),
                            ("NOTPAY", "NOTPAY"),
                            ("PAYERROR", "PAYERROR"),
                            ("REFUND", "REFUND"),
                            ("REVOKED", "REVOKED"),
                            ("SUCCESS", "SUCCESS"),
                            ("USERPAYING", "USERPAYING"),
                        ],
                        max_length=32,
                        verbose_name="trade_state",
                    ),
                ),
                (
                    "time_end",
                    wechat_django.pay.models.base.PayDateTimeField(
                        null=True, verbose_name="pay time_end"
                    ),
                ),
                (
                    "settlement_total_fee",
                    models.PositiveIntegerField(
                        null=True, verbose_name="settlement_total_fee"
                    ),
                ),
                (
                    "cash_fee",
                    models.PositiveIntegerField(null=True, verbose_name="cash_fee"),
                ),
                (
                    "cash_fee_type",
                    models.CharField(
                        max_length=16, null=True, verbose_name="cash_fee_type"
                    ),
                ),
                (
                    "coupon_fee",
                    models.PositiveIntegerField(null=True, verbose_name="coupon_fee"),
                ),
                (
                    "bank_type",
                    models.CharField(
                        max_length=16, null=True, verbose_name="bank_type"
                    ),
                ),
                (
                    "detail",
                    models.TextField(max_length=8192, null=True, verbose_name="detail"),
                ),
                (
                    "is_subscribe",
                    wechat_django.pay.models.base.PayBooleanField(
                        null=True, verbose_name="is_subscribe"
                    ),
                ),
                (
                    "sub_is_subscribe",
                    wechat_django.pay.models.base.PayBooleanField(
                        null=True, verbose_name="sub_is_subscribe"
                    ),
                ),
                ("ext_info", models.JSONField(default=dict, editable=False)),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="updated at"),
                ),
                (
                    "order",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="result",
                        to="wechat_django_pay.unifiedorder",
                    ),
                ),
            ],
            options={
                "verbose_name": "Unified order result",
                "verbose_name_plural": "Unified order results",
            },
        ),
        migrations.AddField(
            model_name="unifiedorder",
            name="pay",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to="wechat_django_pay.wechatpay",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="unifiedorder",
            unique_together={("pay", "out_trade_no")},
        ),
        migrations.AlterIndexTogether(
            name="unifiedorder",
            index_together={("pay", "created_at")},
        ),
    ]

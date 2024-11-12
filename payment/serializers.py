from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from payment.models import PagsmilePayout, UserPayin, WechatPayout


class PagsmilePayoutSerializer(ModelSerializer):
    pay = serializers.SerializerMethodField()

    class Meta:
        model = PagsmilePayout
        fields = ("id", "pay", "status", "updated")

    def get_pay(self, instance):
        return instance.amount


class WechatPayoutSerializer(ModelSerializer):
    workflow_title = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    currency = serializers.SerializerMethodField()

    class Meta:
        model = WechatPayout
        fields = ("id", 'workflow_title', "pay", "status", 'currency', "updated")

    def get_currency(self, instance):
        return "$" if instance.currency == 'USD' else "¥"

    def get_status(self, instance):
        if instance.status == 'success':
            return "已付款"
        return ""

    def get_workflow_title(self, instance):
        return instance.workflow.title


class UserPayinSerializer(ModelSerializer):
    pay = serializers.SerializerMethodField()
    workflow_title = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    currency = serializers.SerializerMethodField()

    class Meta:
        model = UserPayin
        fields = ("workflow_title", "id", "pay", "currency", "status", "updated")

    def get_pay(self, instance):
        return instance.fee

    def get_currency(self, instance):
        return "$" if instance.currency == 'USD' else "¥"

    def get_status(self, instance):
        if instance.status == 'success':
            return "已付款"
        return ""

    def get_workflow_title(self, instance):
        return instance.workflow.title

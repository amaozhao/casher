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
    class Meta:
        model = WechatPayout
        fields = ("id", "pay", "status", "updated")


class UserPayinSerializer(ModelSerializer):
    pay = serializers.SerializerMethodField()

    class Meta:
        model = UserPayin
        fields = ("id", "pay", "currency", "status", "updated")

    def get_pay(self, instance):
        return instance.fee

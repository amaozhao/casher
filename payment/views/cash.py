import uuid

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from allauth.socialaccount.models import SocialAccount
from payment.models import PagsmilePayout, UserPayin, WechatPayout
from payment.serializers import (
    PagsmilePayoutSerializer,
    UserPayinSerializer,
    WechatPayoutSerializer,
)


class CashOutListView(APIView):

    def get(self, requet, *args, **kwargs):
        user = requet.user
        social_account = SocialAccount.objects.filter(user=user).first()
        if social_account and social_account.get_provider() == "google":
            payouts = PagsmilePayout.objects.filter(user=user).all()
            serializer = PagsmilePayoutSerializer(payouts, many=True)
            return Response({"data": serializer.data, "status": status.HTTP_200_OK})
        payouts = WechatPayout.objects.filter(user=user).all()
        serializer = WechatPayoutSerializer(payouts, many=True)
        return Response({"data": serializer.data, "status": status.HTTP_200_OK})


class CashInListView(APIView):

    def get(self, requet, *args, **kwargs):
        user = requet.user
        payins = UserPayin.objects.filter(user=user).all()
        serializer = UserPayinSerializer(payins, many=True)
        return Response({"data": serializer.data, "status": status.HTTP_200_OK})

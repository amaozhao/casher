from app01 import models
from rest_framework.serializers import ModelSerializer


class User_ser(ModelSerializer):
    class Meta:
        model = models.Wxuser
        fields = "__all__"

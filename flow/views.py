import json

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from flow.models import FlowData
from flow.serializers.flowdata import FlowDataSerializer
from flow.utils import generate_qrcode, get_access_token


class FlowList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        flows = FlowData.objects.all()
        serializer = FlowDataSerializer(flows, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FlowDataSerializer(data=request.data)
        if serializer.is_valid():
            fd = FlowData(
                user=User.objects.get(id=1),
                workflow=json.dumps(serializer.data.get('workflow')),
                prompt=json.dumps(serializer.data.get('prompt'))
            )
            fd.save()
            return Response({"message": "成功"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WechatProgramLoginImage(APIView):
    def get(self, request, format=None):
        appid = "your_appid_here"
        secret = "your_secret_here"

        # 获取 access_token
        access_token = get_access_token(appid, secret)
        qrcode = generate_qrcode(access_token)
        return Response({'qrcode': qrcode})


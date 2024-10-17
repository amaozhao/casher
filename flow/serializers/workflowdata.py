from rest_framework import serializers

from flow.models import WorkFlowData


class WorkFlowDataSerializer(serializers.Serializer):
    client_id = serializers.CharField(required=True)
    workflow = serializers.JSONField(required=True)
    prompt = serializers.JSONField(required=True)

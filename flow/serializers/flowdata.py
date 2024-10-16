from rest_framework import serializers

from flow.models import FlowData


class FlowDataSerializer(serializers.Serializer):
    user = serializers.IntegerField(read_only=True)
    workflow = serializers.JSONField(required=True)
    prompt = serializers.JSONField(required=True)

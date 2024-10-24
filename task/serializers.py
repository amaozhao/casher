from rest_framework import serializers
from task.models import TaskResult


class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField(required=True)


class TaskSerializer(serializers.Serializer):
    image = serializers.CharField(required=True)
    desc = serializers.CharField(required=True)


class TaskResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskResult
        fields = ['id', 'result', 'created']

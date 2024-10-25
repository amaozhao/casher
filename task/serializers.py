from urllib.parse import urljoin
from rest_framework import serializers
from task.models import TaskResult


class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField(required=True)


class TaskSerializer(serializers.Serializer):
    image = serializers.CharField(required=True)
    desc = serializers.CharField(required=True)


class TaskResultSerializer(serializers.ModelSerializer):
    result = serializers.SerializerMethodField()
    workflow_id = serializers.SerializerMethodField()

    class Meta:
        model = TaskResult
        fields = ['id', 'result', 'created', 'workflow_id']

    def get_result(self, instance):
        return urljoin("http://aidep.cn:8601", instance.result.url)

    def get_workflow_id(self, instance):
        task = instance.task
        return task.flow.id

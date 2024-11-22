from urllib.parse import urljoin
from datetime import datetime, timedelta

from rest_framework import serializers

from task.models import TaskResult


class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField(required=True)


class TaskSerializer(serializers.Serializer):
    image = serializers.CharField(required=True)
    desc = serializers.CharField(required=True)


class TaskResultSerializer(serializers.ModelSerializer):
    jilu_id = serializers.SerializerMethodField()
    result = serializers.SerializerMethodField()
    workflow_id = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = TaskResult
        fields = ["id", "result", "status", "created", "workflow_id", "jilu_id"]

    def get_result(self, instance):
        return (
            urljoin("https://aidep.cn", instance.result.url)
            if instance.result
            else None
        )

    def get_workflow_id(self, instance):
        task = instance.task
        return task.flow.id

    def get_jilu_id(self, instance):
        task = instance.task
        return task.jilu_id

    def get_status(self, instance):
        task = instance.task
        if (
            datetime.now().replace(tzinfo=None) - task.created.replace(tzinfo=None)
            > timedelta(hours=1)
            and task.status == "queue"
        ):
            return "fail"
        return task.status

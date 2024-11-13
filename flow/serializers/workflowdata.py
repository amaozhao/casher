from urllib.parse import urljoin
import random

from rest_framework import serializers

from flow.models import WorkFlowComment, WorkFlowData, WorkFlowImage


class WorkFlowImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = WorkFlowImage
        fields = ["id", "image"]

    def get_image(self, instance):
        return urljoin("https://aidep.cn", instance.image.url)


class WorkFlowDataSerializer(serializers.ModelSerializer):
    images = WorkFlowImageSerializer(many=True)
    workflow_fields = serializers.SerializerMethodField()
    consuming = serializers.SerializerMethodField()

    class Meta:
        model = WorkFlowData
        fields = [
            "id",
            "title",
            "gn_desc",
            "sy_desc",
            "fee",
            "free_times",
            "uniqueid",
            "client_id",
            "created",
            "updated",
            "images",
            "status",
            "deleted",
            "workflow_fields",
            "consuming",
        ]

    def get_workflow_fields(self, instance):
        post_data = instance.post_data
        result = {
            "cs_img_nodes": post_data.get("cs_img_nodes"),
            "cs_text_nodes": post_data.get("cs_text_nodes"),
            "cs_video_nodes": post_data.get("cs_video_nodes"),
        }
        return result

    def get_consuming(self, instance):
        from task.models import TaskResult

        t_result = TaskResult.objects.filter(
            task__flow=instance, result__isnull=False, task__status="success"
        ).first()
        if t_result:
            return int((t_result.updated - t_result.created).total_seconds()) + 3
        return random.randint(10, 30)

    image = serializers.SerializerMethodField()


class BWorkFlowDataSerializer(WorkFlowDataSerializer):
    preview_url = serializers.SerializerMethodField()

    class Meta:
        model = WorkFlowData
        fields = [
            "id",
            "title",
            "gn_desc",
            "sy_desc",
            "fee",
            "free_times",
            "uniqueid",
            "client_id",
            "created",
            "updated",
            "images",
            "status",
            "deleted",
            "preview_url",
        ]

    def get_preview_url(self, instance):
        result = f"https://aidep.cn/?workflow_id={instance.id}"
        return result


class WorkFlowCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkFlowComment
        fields = [
            "id",
            "comment",
        ]

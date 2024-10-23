from rest_framework import serializers

from flow.models import WorkFlowData, WorkFlowImage, WorkFlowComment


class WorkFlowImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkFlowImage
        fields = ["id", "image"]


class WorkFlowDataSerializer(serializers.ModelSerializer):
    images = WorkFlowImageSerializer(many=True)

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
        ]


class WorkFlowCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkFlowComment
        fields = [
            "id",
            "comment",
        ]

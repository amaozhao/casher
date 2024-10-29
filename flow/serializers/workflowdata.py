from urllib.parse import urljoin

from rest_framework import serializers

from flow.models import WorkFlowComment, WorkFlowData, WorkFlowImage


class WorkFlowImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = WorkFlowImage
        fields = ["id", "image"]

    def get_image(self, instance):
        return urljoin("http://aidep.cn:8601", instance.image.url)


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

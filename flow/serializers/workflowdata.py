from urllib.parse import urljoin

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
    fields = serializers.SerializerMethodField()

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
            "fields",
        ]

    def get_fields(self, instance):
        post_data = instance.post_data
        result = {
            'cs_img_nodes': post_data.get('cs_img_nodes'),
            'cs_text_nodes': post_data.get('cs_text_nodes'),
            'cs_video_nodes': post_data.get('cs_video_nodes'),
        }
        return result


class WorkFlowCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkFlowComment
        fields = [
            "id",
            "comment",
        ]

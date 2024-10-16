from rest_framework import serializers


class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField(required=True)


class TaskSerializer(serializers.Serializer):
    image = serializers.CharField(required=True)
    desc = serializers.CharField(required=True)

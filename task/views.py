import os

from django.http import FileResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser

from task.models import UserUpload
from task.services import comfy_service
from task.consumer import client_dict


class ImageUploadView(APIView):
    """
    处理图像上传，将图像传递给外部服务，并将相关信息存储到数据库中。
    """

    def post(self, request, *args, **kwargs):
        image_file = request.FILES.get("filePath")
        if not image_file:
            return Response(
                {"error": "No image file provided."}, status=status.HTTP_400_BAD_REQUEST
            )

        # 保存上传记录到数据库
        user_upload = UserUpload(
            user_id=1,  # 假设这里是固定用户ID，未来可以扩展为动态用户
            image=image_file,
        )
        user_upload.save()

        return Response(
            {
                "message": "Image uploaded and forwarded successfully!",
                "user_upload": {
                    "image": request.build_absolute_uri(user_upload.image.url),
                },
            },
            status=status.HTTP_201_CREATED,
        )


class PromptView(APIView):
    """
    处理前端提交的提示和图像描述，整合数据并提交给外部服务。
    """

    def post(self, request, *args, **kwargs):
        prompt_message = {
            "type": "prompt",
            "uniqueid": "m2ebqnbknfcdp57cg96nryw5nv",
            "data": {
                "jilu_id": "67890xyz",
                "cs_imgs": [
                    {
                        "upImage": "http://192.168.10.104:8000/media/user/images/%E7%BE%8E%E5%A5%B3.png",
                        "node": "29",
                    }
                ],
                "cs_videos": [],
                "cs_texts": [
                    {"node": "50", "value": "This is a sample text for node 4."}
                ],
            },
        }

        # 获取 Channels 的 layer
        channel_layer = get_channel_layer()
        client_id = "80fd42e0-d652-4732-b209-e14edd0cc217:8188"
        wss = client_dict.get(client_id)

        async_to_sync(channel_layer.send)(wss, prompt_message)
        return Response({"message": "任务提交成功"}, status=status.HTTP_200_OK)


class PromptCompleted(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        # image_file = request.FILES.get("image")
        # if not image_file:
        #     return Response(
        #         {"error": "No image file provided."}, status=status.HTTP_400_BAD_REQUEST
        #     )
        #
        # # 保存上传记录到数据库
        # user_upload = UserUpload(
        #     user_id=1,  # 假设这里是固定用户ID，未来可以扩展为动态用户
        #     image=image_file,
        # )
        # user_upload.save()
        print(1111, request.data)
        print(2222, request.FILES)
        print(3333, request.content_type)

        return Response(
            {
                "message": "Image uploaded and forwarded successfully!",
            },
            status=status.HTTP_201_CREATED,
        )


class ImageDisplayView(APIView):
    """
    根据请求参数从外部服务获取图像并返回给前端。
    """

    def get(self, request, *args, **kwargs):
        filename = request.GET.get("filename")
        subfolder = request.GET.get("subfolder")
        image_type = request.GET.get("type")

        if not all([filename, subfolder, image_type]):
            return Response(
                {"error": "Invalid parameters."}, status=status.HTTP_400_BAD_REQUEST
            )

        # 从 comfy_service 获取图像数据
        image_data = comfy_service.fetch_image(filename, subfolder, image_type)
        if not image_data:
            return Response(
                {"error": "Image not found."}, status=status.HTTP_404_NOT_FOUND
            )

        # 保存图像到本地
        image_path = self._save_image_to_local(subfolder, filename, image_data)

        return FileResponse(open(image_path, "rb"))

    @staticmethod
    def _save_image_to_local(subfolder, filename, image_data):
        """
        将图像保存到本地目录。

        参数:
        - subfolder: 子文件夹名。
        - filename: 文件名。
        - image_data: 图像的二进制数据。

        返回:
        - 图像的完整本地路径。
        """
        image_dir = f"./media/{subfolder}"
        os.makedirs(image_dir, exist_ok=True)
        image_path = f"{image_dir}/{filename}"

        with open(image_path, "wb") as image_file:
            image_file.write(image_data)

        return image_path

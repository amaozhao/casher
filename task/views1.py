import uuid

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser

from flow.models import WorkFlowData
from task.models import UserUpload, UserTask, TaskResult
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
        jilu_id = str(uuid.uuid4())
        # workflow_id = request.data.get('workflow_id')
        # image_id = request.data.get('image_id')
        # prompt_text = request.data.get('prompt_text')
        prompt_message = {
            "type": "prompt",
            "uniqueid": "m2ebqnbknfcdp57cg96nryw5nv",
            "data": {
                "jilu_id": "jilu_id",
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
        client_id = "80fd42e0-d652-4732-b209-e14edd0cc217"
        # workflow = WorkFlowData.objects.get(id=workflow_id)
        # image = UserUpload.objects.get(id=image_id)
        # workflow_fee = workflow.fee
        # workflow_free_times = workflow.free_times
        # user_task = UserTask(
        #     jilu_id=jilu_id,
        #     workflow_id=workflow,
        #     image=image,
        #     prompt_text=prompt_text
        # )
        wss = client_dict.get(client_id)
        print(wss)
        async_to_sync(channel_layer.send)(wss, prompt_message)
        return Response({"message": "任务提交成功"}, status=status.HTTP_200_OK)


class PromptCompleted(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        prompt_id = request.data.get('prompt_id')
        print(1111, prompt_id)
        # user_task = UserTask.objects.filter(prompt_id=prompt_id).first()
        # if not user_task:
        #     return Response(
        #         {"error": "prompt_id not found."}, status=status.HTTP_400_BAD_REQUEST
        #     )
        # image_file = request.FILES.get('file[]')
        print(2222, request.FILES)

        # if not image_file:
        #     return Response(
        #         {"error": "No image file provided."}, status=status.HTTP_400_BAD_REQUEST
        #     )
        # # 保存上传记录到数据库
        # task_result = TaskResult(
        #     user_task=user_task,
        #     result=image_file
        # )
        # task_result.save()

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
        jilu_id = request.data.get('jilu_id')
        user_task = UserTask.objects.filter(jilu_id=jilu_id).first()
        if not user_task:
            return Response(
                {"error": "Invalid parameters."}, status=status.HTTP_400_BAD_REQUEST
            )
        task_result = TaskResult.objects.filter(user_task=user_task).first()

        return Response(
            {"url": task_result.result.url}, status=status.HTTP_200_OK
        )

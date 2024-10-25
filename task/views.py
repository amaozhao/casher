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
from task.serializers import TaskResultSerializer


class ImageUploadView(APIView):
    """
    处理图像上传，将图像传递给外部服务，并将相关信息存储到数据库中。
    """

    def post(self, request, *args, **kwargs):
        print(request.FILES)
        print(request.data)
        image_file = request.FILES.get("file")
        if not image_file:
            return Response(
                {"data": {"error": "No image file provided."}, 'status': status.HTTP_200_OK},
                status=status.HTTP_400_BAD_REQUEST
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
                "data": {
                    "image": request.build_absolute_uri(user_upload.image.url),
                    'id': user_upload.id,
                },
                'status': status.HTTP_200_OK
            },
            status=status.HTTP_201_CREATED,
        )


class PromptView(APIView):
    """
    处理前端提交的提示和图像描述，整合数据并提交给外部服务。
    """

    def post(self, request, *args, **kwargs):
        jilu_id = str(uuid.uuid4())
        workflow_id = request.data.get('workflow_id')
        image_url = request.data.get('image_url')
        # image_id = request.data.get('image_id', 1)
        # user_upload = UserUpload.objects.filter(id=image_id).first()
        prompt_text = request.data.get('prompt_text')
        workflow = WorkFlowData.objects.filter(id=workflow_id).first()
        cs_img_nodes = workflow.post_data.get('cs_img_nodes')
        cs_text_nodes = workflow.post_data.get('cs_text_nodes')
        uniqueid = request.data.get('uniqueid')
        user_task = UserTask(
            jilu_id=jilu_id,
            flow=workflow,
            fee=workflow.fee,
            prompt_text=prompt_text,
            # image
        )
        user_task.save()
        prompt_message = {
            "type": "prompt",
            "uniqueid": uniqueid,
            "data": {
                "jilu_id": jilu_id,
                "cs_imgs": [
                    {
                        "upImage": image_url,
                        "node": cs_img_nodes[0].get('node'),
                    }
                ],
                "cs_videos": [],
                "cs_texts": [
                    {"node": cs_text_nodes[0].get('node'), "value": prompt_text}
                ],
            },
        }

        # 获取 Channels 的 layer
        channel_layer = get_channel_layer()
        client_id = workflow.client_id
        wss = client_dict.get(client_id)
        async_to_sync(channel_layer.send)(wss, prompt_message)
        return Response({"message": "任务提交成功", "jilu_id": jilu_id}, status=status.HTTP_200_OK)


class PromptCompleted(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        image_file = request.FILES.get("file")
        prompt_id = request.data.get('prompt_id')
        user_task = UserTask.objects.filter(prompt_id=prompt_id).first()
        task_result = TaskResult(
            task=user_task,
            result=image_file
        )
        task_result.save()
        query = TaskResult.objects.filter(task=user_task)
        if query.count() > 1:
            last = query.order_by('-updated').first()
            _query = TaskResult.objects.filter(task=user_task).exclude(id=last.id)
            for obj in _query:
                obj.delete()

        return Response(
            {
                "message": "Image uploaded and forwarded successfully!",
                "status": status.HTTP_200_OK
            },
            status=status.HTTP_201_CREATED,
        )


class ImageDisplayView(APIView):
    """
    根据请求参数从外部服务获取图像并返回给前端。
    """

    def get(self, request, *args, **kwargs):
        jilu_id = request.GET.get('jilu_id')
        user_task = UserTask.objects.filter(jilu_id=jilu_id).first()
        result = TaskResult.objects.filter(task=user_task).order_by("-updated").first()
        return Response({'url': request.build_absolute_uri(result.result.url)}, status=status.HTTP_200_OK)


class TaskHistoryView(APIView):
    def get(self, request, *args, **kwargs):
        query = TaskResult.objects.all()
        serializer = TaskResultSerializer(query, many=True, context={'request': None})
        return Response({'data': serializer.data, 'status': status.HTTP_200_OK})

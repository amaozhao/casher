import uuid

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from flow.models import WorkFlowData
from payment.models import UserHashrate
from task.consumer import client_dict
from task.models import TaskFreeCount, TaskResult, UserTask, UserUpload
from task.serializers import TaskResultSerializer
import logging

logger = logging.getLogger('channel')


class ImageUploadView(APIView):
    """
    处理图像上传，将图像传递给外部服务，并将相关信息存储到数据库中。
    """

    def post(self, request, *args, **kwargs):
        image_file = request.FILES.get("file")
        if not image_file:
            return Response(
                {
                    "data": {"error": "No image file provided."},
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_400_BAD_REQUEST,
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
                    "id": user_upload.id,
                },
                "status": status.HTTP_200_OK,
            },
            status=status.HTTP_201_CREATED,
        )


class PromptView(APIView):
    """
    处理前端提交的提示和图像描述，整合数据并提交给外部服务。
    """

    def post(self, request, *args, **kwargs):
        jilu_id = str(uuid.uuid4())
        workflow_id = request.data.get("workflow_id")
        image_url = request.data.get("image_url", "")
        prompt_text = request.data.get("prompt_text", "")
        workflow = WorkFlowData.objects.filter(id=workflow_id).first()
        task_free_count = TaskFreeCount.objects.filter(workflow=workflow).first()
        if task_free_count and task_free_count.free_count >= workflow.free_times:
            hashrate = UserHashrate.objects.filter(user=request.user).first()
            if not hashrate:
                hashrate = UserHashrate.objects.create(user=request.user)
            if hashrate.hashrate < workflow.fee:
                return Response(
                    {
                        "data": {"jilu_id": jilu_id},
                        "message": "余额不足，请充值",
                        "status": status.HTTP_400_BAD_REQUEST,
                    },
                    status=status.HTTP_200_OK,
                )
        cs_img_nodes = workflow.post_data.get("cs_img_nodes")
        cs_text_nodes = workflow.post_data.get("cs_text_nodes")
        uniqueid = workflow.uniqueid
        user_task = UserTask(
            user=request.user,
            jilu_id=jilu_id,
            flow=workflow,
            fee=workflow.fee,
            prompt_text=prompt_text,
        )
        user_task.save()
        prompt_message = {
            "type": "prompt",
            "uniqueid": uniqueid,
            "data": {
                "jilu_id": jilu_id,
                "cs_videos": [],
                "cs_texts": [],
            },
        }
        if cs_text_nodes:
            prompt_message['data']['cs_texts'] = [{"node": cs_text_nodes[0].get("node"), "value": prompt_text}]
        if cs_img_nodes:
            if not image_url:
                return Response(
                    {
                        "message": "缺少参数image_url",
                        "jilu_id": jilu_id,
                        "status": status.HTTP_400_BAD_REQUEST,
                    },
                    status=status.HTTP_200_OK,
                )
            prompt_message["data"]["cs_imgs"] = [
                {
                    "upImage": image_url,
                    "node": cs_img_nodes[0].get("node"),
                }
            ]

        if cs_text_nodes:
            if not prompt_text:
                return Response(
                    {
                        "message": "缺少参数 prompt_text",
                        "jilu_id": jilu_id,
                        "status": status.HTTP_400_BAD_REQUEST,
                    },
                    status=status.HTTP_200_OK,
                )
            prompt_message["data"]["cs_texts"] = [
                {"node": cs_text_nodes[0].get("node"), "value": prompt_text}
            ]

        # 获取 Channels 的 layer
        channel_layer = get_channel_layer()
        client_id = workflow.client_id
        wss = client_dict.get(client_id)
        logger.info(f"client_id: {client_id}, wss: {wss}")
        if not wss:
            return Response(
            {
                "data": {"jilu_id": jilu_id},
                "message": "wss 连接失败，请检查ComfyUI设置是否正确",
                "status": status.HTTP_400_BAD_REQUEST,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
        async_to_sync(channel_layer.send)(wss, prompt_message)
        return Response(
            {
                "data": {"jilu_id": jilu_id},
                "message": "任务提交成功",
                "status": status.HTTP_200_OK,
            },
            status=status.HTTP_200_OK,
        )


class PromptCompleted(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        image_file = request.FILES.get("file")
        prompt_id = request.data.get("prompt_id")
        user_task = UserTask.objects.filter(prompt_id=prompt_id).first()
        task_result = TaskResult(task=user_task, result=image_file)
        task_result.save()
        query = TaskResult.objects.filter(task=user_task)
        if query.count() > 1:
            last = query.order_by("-updated").first()
            _query = TaskResult.objects.filter(task=user_task).exclude(id=last.id)
            for obj in _query:
                obj.delete()

        return Response(
            {
                "message": "Image uploaded and forwarded successfully!",
                "status": status.HTTP_200_OK,
            },
            status=status.HTTP_201_CREATED,
        )


class ImageDisplayView(APIView):
    """
    根据请求参数从外部服务获取图像并返回给前端。
    """

    def get(self, request, *args, **kwargs):
        jilu_id = request.GET.get("jilu_id")
        user_task = UserTask.objects.filter(jilu_id=jilu_id).first()
        result = TaskResult.objects.filter(task=user_task).order_by("-updated").first()
        if not result or not result.result:
            return Response(
                {"data": None, "status": status.HTTP_200_OK}, status=status.HTTP_200_OK
            )
        return Response(
            {
                "data": {"url": request.build_absolute_uri(result.result.url)},
                "status": status.HTTP_200_OK,
            },
            status=status.HTTP_200_OK,
        )


class TaskHistoryView(APIView):
    def get(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        query = UserTask.objects.filter(user=user)
        workflow_id = data.get('workflow_id')
        if workflow_id:
            workflow = WorkFlowData.objects.filter(id=workflow_id).first()
            query = query.filter(flow=workflow).all()
        serializer = TaskResultSerializer(query, many=True, context={"request": None})
        return Response({"data": serializer.data, "status": status.HTTP_200_OK})


class TaskHistoryDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        task = TaskResult.objects.get(id=id)
        task.result.delete(save=True)
        task.delete()
        return Response({"data": {}, "status": status.HTTP_204_NO_CONTENT})

from django.contrib.auth.models import User
from rest_framework.views import APIView

from flow.models import WorkFlowData, ImageNode, VideoNode
from flow.serializers.workflowdata import WorkFlowDataSerializer
from flow.utils import generate_qrcode, get_access_token
from rest_framework.response import Response
from rest_framework import status
import json


class UploadAPIView(APIView):
    """
    处理来自前端的 postData 上传，并根据 techsid 和 r 值执行不同的逻辑
    """

    def post(self, request):
        # 获取 URL 中的参数 techsid 和 r
        r_value = request.GET.get("r")
        techsid = request.GET.get("techsid")

        if not r_value or not techsid:
            return Response({"error": "Missing 'r' or 'techsid' in URL"}, status=status.HTTP_400_BAD_REQUEST)

        # 解析表单中的 json_data
        json_data = request.POST.get("json_data", None)

        if not json_data:
            return Response({"error": "Missing json_data"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            post_data = json.loads(json_data)  # 解析 json_data
        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON data"}, status=status.HTTP_400_BAD_REQUEST)

        # 处理文件上传
        cs_img_files = request.FILES.getlist('cs_img_files', [])
        cs_video_files = request.FILES.getlist('cs_video_files', [])

        # 根据 r 的值执行不同的逻辑
        if r_value == "comfyui.apiv2.upload":
            return self.handle_upload(post_data, cs_img_files, cs_video_files, techsid)
        elif r_value == "comfyui.apiv2.code":
            return self.handle_code_logic(post_data, techsid)
        else:
            return Response({"error": f"Unsupported r value: {r_value}"}, status=status.HTTP_400_BAD_REQUEST)

    def handle_upload(self, post_data, cs_img_files, cs_video_files, techsid):
        """
        处理上传逻辑，并将数据保存到数据库
        """
        try:
            # 创建 PostData 实例并保存
            post_data_instance = WorkFlowData.objects.create(
                client_id=post_data.get("client_id"),
                techsid=techsid,
                res_node=post_data.get("res_node"),
                main_images=post_data.get("mainImages", []),
                title=post_data.get("title"),
                gn_desc=post_data.get("gn_desc"),
                sy_desc=post_data.get("sy_desc"),
                fee=post_data.get("fee"),
                free_times=post_data.get("free_times"),
                uniqueid=post_data.get("uniqueid"),
                output=post_data.get("output", {}),
                workflow=post_data.get("workflow", {})
            )

            # 处理图片节点上传
            cs_img_descs = post_data.get("cs_img_nodes", [])
            for index, img_file in enumerate(cs_img_files):
                desc = cs_img_descs[index].get('desc', '') if index < len(cs_img_descs) else ''
                ImageNode.objects.create(post_data=post_data_instance, image=img_file, desc=desc)

            # 处理视频节点上传
            cs_video_descs = post_data.get("cs_video_nodes", [])
            for index, video_file in enumerate(cs_video_files):
                desc = cs_video_descs[index].get('desc', '') if index < len(cs_video_descs) else ''
                VideoNode.objects.create(post_data=post_data_instance, video=video_file, desc=desc)

            return Response(
                {"message": "PostData saved successfully", "id": post_data_instance.id},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def handle_code_logic(self, post_data, techsid):
        """
        处理与 code 相关的逻辑
        """
        # 示例处理逻辑，可以根据需要自定义
        return Response({
            "message": f"Handling code logic for techsid: {techsid}",
            "data": post_data
        }, status=status.HTTP_200_OK)


class FlowList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        flows = WorkFlowData.objects.all()
        serializer = WorkFlowDataSerializer(flows, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WorkFlowDataSerializer(data=request.data)
        if serializer.is_valid():
            fd = WorkFlowData(
                user=User.objects.get(id=1),
                workflow=json.dumps(serializer.data.get("workflow")),
                prompt=json.dumps(serializer.data.get("prompt")),
            )
            fd.save()
            return Response({"message": "成功"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WechatProgramLoginImage(APIView):
    def get(self, request, format=None):
        appid = "your_appid_here"
        secret = "your_secret_here"

        # 获取 access_token
        access_token = get_access_token(appid, secret)
        qrcode = generate_qrcode(access_token)
        return Response({"qrcode": qrcode})

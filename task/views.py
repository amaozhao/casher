import json
import os
import random

from django.http import FileResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from task.services import comfy_service
from task.models import UserUpload, UserTask
from flow.models import FlowData


class ImageUploadView(APIView):
    """
    处理图像上传，将图像传递给外部服务，并将相关信息存储到数据库中。
    """

    def post(self, request, *args, **kwargs):
        image_file = request.FILES.get('image')
        if not image_file:
            return Response({'error': 'No image file provided.'}, status=status.HTTP_400_BAD_REQUEST)

        # 上传图片至comfy_service
        upload_response = comfy_service.upload_image(image_file)
        if not upload_response:
            return Response({'error': 'Image upload failed on external service.'}, status=status.HTTP_400_BAD_REQUEST)

        # 保存上传记录到数据库
        user_upload = UserUpload(
            user_id=1,  # 假设这里是固定用户ID，未来可以扩展为动态用户
            name=upload_response.get('name'),
            subfolder=upload_response.get('subfolder'),
        )
        user_upload.save()

        return Response({
            'message': 'Image uploaded and forwarded successfully!',
            'user_upload': {
                'name': user_upload.name,
                'subfolder': user_upload.subfolder,
                'uid': user_upload.uid,
            }
        }, status=status.HTTP_201_CREATED)


class PromptView(APIView):
    """
    处理前端提交的提示和图像描述，整合数据并提交给外部服务。
    """

    def post(self, request, *args, **kwargs):
        uid = request.data.get('uid')
        desc = request.data.get('desc')

        if not uid or not desc:
            return Response({'error': 'Both uid and desc are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # 获取上传的图像记录
        user_upload = UserUpload.objects.filter(uid=uid).first()
        if not user_upload:
            return Response({'error': 'Invalid uid.'}, status=status.HTTP_404_NOT_FOUND)

        # 获取流程数据
        flow_data = FlowData.objects.get(id=1)
        workflow_data = json.loads(flow_data.workflow)
        promt_data = json.loads(flow_data.prompt)

        # 更新提示数据中的描述和图像信息
        self._update_prompt_with_desc(workflow_data, promt_data, desc, user_upload)

        api_data = {
            'client_id': random.randint(10 ** 15, 10 ** 16 - 1),
            'prompt': promt_data
        }

        # 提交修改后的数据至外部服务
        response = comfy_service.send_prompt(api_data)
        if response:
            prompt_id = response.get('prompt_id')
            # 保存任务记录
            task = UserTask(
                user_id=1,  # 假设固定用户ID，未来可以扩展为动态用户
                flow=flow_data,
                prompt_id=prompt_id,
                result=''
            )
            task.save()

            return Response({
                'message': '任务提交成功',
                'prompt_id': prompt_id
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': '任务提交失败，请重试'}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def _update_prompt_with_desc(workflow_data, prompt_data, desc, user_upload):
        """
        更新提示中的描述信息和图像链接。

        参数:
        - workflow_data: 工作流的提示数据。
        - workflow_data: 提示对应的输出数据。
        - desc: 用户提交的描述信息。
        - user_upload: 用户上传的图像记录。
        """

        def get_link_by_id(link_id, links):
            for link in links:
                if link[0] == link_id:
                    return link[1]
            return None

        # 遍历节点，找到需要更新的内容
        nodes = workflow_data['nodes']
        links = workflow_data['links']
        for node in nodes:
            if node.get('class_type') == 'sdCash':
                node['inputs']['custom_text1_desc'] = desc

                # 更新图像节点和描述节点
                for input_node in node['inputs']:
                    if input_node.get('name') == 'custom_img1(optional)':
                        link_id = get_link_by_id(input_node.get('link'), links)
                        if link_id:
                            prompt_data[link_id]['inputs']['image'] = user_upload.name
                            prompt_data[link_id]['inputs']['upload'] = user_upload.subfolder
                    elif input_node.get('name') == 'custom_text1(optional)':
                        link_id = get_link_by_id(input_node.get('link'), links)
                        if link_id:
                            prompt_data[link_id]['inputs']['text'] = desc


class ImageDisplayView(APIView):
    """
    根据请求参数从外部服务获取图像并返回给前端。
    """

    def get(self, request, *args, **kwargs):
        filename = request.GET.get('filename')
        subfolder = request.GET.get('subfolder')
        image_type = request.GET.get('type')

        if not all([filename, subfolder, image_type]):
            return Response({'error': 'Invalid parameters.'}, status=status.HTTP_400_BAD_REQUEST)

        # 从 comfy_service 获取图像数据
        image_data = comfy_service.fetch_image(filename, subfolder, image_type)
        if not image_data:
            return Response({'error': 'Image not found.'}, status=status.HTTP_404_NOT_FOUND)

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
        image_dir = f'./media/{subfolder}'
        os.makedirs(image_dir, exist_ok=True)
        image_path = f'{image_dir}/{filename}'

        with open(image_path, 'wb') as image_file:
            image_file.write(image_data)

        return image_path

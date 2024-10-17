import base64
from asgiref.sync import async_to_sync
from task.consumer import ClientConsumer

class ComfyUIService:
    def __init__(self, comfy_ui_service):
        self.comfy_ui_service = comfy_ui_service  # 传入异步服务类实例

    def upload_image(self, client_id, image_file, image_type="input", overwrite=False):
        """
        同步上传图片，通过 async_to_sync 调用异步方法，同时保留对 image_data 的组装逻辑。
        """
        # 组装 image_data
        image_data = {
            "filename": image_file.name,
            "file_content": base64.b64encode(image_file.read()).decode('utf-8'),
            "image_type": image_type,
            "overwrite": overwrite,
        }

        # 通过 async_to_sync 调用异步的上传方法
        return async_to_sync(self.comfy_ui_service.send_to_ws)(client_id, image_data)

    def prompt(self, client_id, prompt_data):
        """
        同步发送 prompt 任务。
        """
        return async_to_sync(self.comfy_ui_service.prompt)(client_id, prompt_data)

    def get_history(self, client_id, prompt_id):
        """
        同步获取 prompt 历史记录。
        """
        return async_to_sync(self.comfy_ui_service.get_history)(client_id, prompt_id)

    def fetch_image(self, client_id, filename, subfolder, image_type):
        """
        同步获取图片。
        """
        return async_to_sync(self.comfy_ui_service.fetch_image)(client_id, filename, subfolder, image_type)

    def get_prompt_images(self, client_id, prompt_id):
        """
        同步获取提示生成的所有图片。
        """
        return async_to_sync(self.comfy_ui_service.get_prompt_images)(client_id, prompt_id)

# 使用示例：
# 假设有一个已实例化的异步 ComfyUIService 类 (comfy_ui_service)
# 你可以通过 SyncComfyUIService 来在同步环境中调用：

client_consumer = ClientConsumer(scope={"url_route": {"kwargs": {"client_id": "1234"}}})
comfy_service = ComfyUIService(client_consumer)
# with open("path_to_image_file", "rb") as image_file:
#     result = sync_comfy_service.upload_image(client_id="1234", image_file=image

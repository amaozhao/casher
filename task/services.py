import requests
import json
import websocket
import uuid


class ComfyUIService:
    def __init__(self, comfy_host='http://192.168.10.100:8189', ws_host='ws://192.168.10.100:8189'):
        self.comfy_host = comfy_host
        self.ws_host = ws_host

    def upload_image(self, image_file, image_type="input", overwrite=False):
        """
        上传图片至Comfy UI服务器。

        参数:
        - image_file: 上传的图片文件对象。
        - image_type: 图片类型，默认为 'input'。
        - overwrite: 是否覆盖现有图片，默认为 False。

        返回:
        - 成功时返回响应的JSON数据，失败时返回None。
        """
        upload_url = f'{self.comfy_host}/upload/image'
        data = {
            "subfolder": "images",
            "type": image_type,
            "overwrite": str(overwrite).lower()
        }
        files = {"image": image_file}

        response = requests.post(upload_url, data=data, files=files)
        return response.json() if response.status_code == 200 else None

    def send_prompt(self, prompt_data):
        """
        向Comfy UI发送提示信息。

        参数:
        - prompt_data: 提示的JSON格式数据。

        返回:
        - 成功时返回响应的JSON数据，失败时返回None。
        """
        prompt_url = f'{self.comfy_host}/prompt'
        response = requests.post(prompt_url, json=prompt_data)
        return response.json() if response.status_code == 200 else None

    def get_prompt_history(self, prompt_id):
        """
        获取特定提示的历史记录。

        参数:
        - prompt_id: 提示的唯一标识符。

        返回:
        - 成功时返回提示历史记录，失败时抛出异常。
        """
        history_url = f"{self.comfy_host}/history/{prompt_id}"
        response = requests.get(history_url)

        if response.status_code == 200:
            result = response.json()
            return result.get(prompt_id)
        else:
            response.raise_for_status()

    def fetch_image(self, filename, subfolder, image_type):
        """
        从服务器获取指定的图片。

        参数:
        - filename: 图片文件名。
        - subfolder: 图片所在子文件夹。
        - image_type: 图片类型。

        返回:
        - 图片的二进制数据。
        """
        image_url = f'{self.comfy_host}/view'
        params = {"filename": filename, "subfolder": subfolder, "type": image_type}

        response = requests.get(image_url, params=params, stream=True)
        if response.status_code == 200:
            return response.content
        else:
            response.raise_for_status()

    def retrieve_images(self, websocket_connection, prompt_id):
        """
        从WebSocket连接中检索图片数据。

        参数:
        - websocket_connection: WebSocket连接对象。
        - prompt_id: 提示的唯一标识符。

        返回:
        - 包含图片的字典，如果没有找到则返回None。
        """
        output_images = {}

        while True:
            message = websocket_connection.recv()
            if isinstance(message, str):
                message = json.loads(message)
            if message['type'] == 'executing' and message['data']['node'] is None:
                if message['data']['prompt_id'] == prompt_id:
                    break
            elif message['type'] == 'crystools.monitor':
                break

        history = self.get_prompt_history(prompt_id)
        if not history:
            return None

        for node_id, node_output in history['outputs'].items():
            images_output = []
            if 'images' in node_output:
                for image_info in node_output['images']:
                    image_data = self.fetch_image(
                        image_info['filename'],
                        image_info['subfolder'],
                        image_info['type']
                    )
                    images_output.append(image_data)
            output_images[node_id] = images_output

        return output_images

    def get_prompt_images(self, prompt_id):
        """
        获取提示生成的所有图片。

        参数:
        - prompt_id: 提示的唯一标识符。

        返回:
        - 返回包含图片数据的字典。
        """
        ws = websocket.WebSocket()
        ws.connect(f"{self.ws_host}/ws?clientId={uuid.uuid4()}")
        images = self.retrieve_images(ws, prompt_id)
        ws.close()
        return images


comfy_service = ComfyUIService()


if __name__ == '__main__':
    comfy_service = ComfyUIService()
    result = comfy_service.get_prompt_images('b2339b0b-0b6f-4dc1-9019-500d13500c78')
    if result and '29' in result:
        print(f"Number of images in node '29': {len(result['29'])}")

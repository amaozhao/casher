from channels.generic.websocket import AsyncWebsocketConsumer
import json
import urllib.parse


class ClientConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # 解析查询参数，提取 clientId
        query_string = self.scope['query_string'].decode('utf-8')
        client_id = self._get_client_id(query_string)

        if client_id:
            print(f"New client connected with clientId: {client_id}")
        else:
            # 没有 clientId，处理旧版客户端情况
            print(f"Old client connected without clientId")

        # 接受 WebSocket 连接
        await self.accept()

    async def _get_client_id(self, query_string):
        # 解析 clientId（如果存在）
        query_params = urllib.parse.parse_qs(query_string)
        return query_params.get('clientId', [None])[0]

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_type = data.get('type')

        # 处理来自客户端的 bind 消息
        if message_type == "crystools.bind":
            await self.handle_bind(data)
        # 移除对 "prompt" 消息的处理，因为这是服务端发给客户端的消息
        if message_type == "crystools.prompt_error":
            await self.handle_prompt_error(data)

    async def handle_bind(self, data):
        client_id = data['data']['client_id']
        print(f"Received bind message from client: {client_id}")

        # 发送 init 消息，确认绑定并返回 client_id
        init_message = {
            "type": "init",
            "data": {
                "client_id": client_id  # 返回给客户端
            }
        }
        await self.send(json.dumps(init_message))

    async def handle_prompt_error(self, data):
        # 处理 prompt_error 消息
        jilu_id = data['data']['jilu_id']
        error_message = data['data']['msg']
        print(f"Received prompt_error message for task {jilu_id}: {error_message}")
        # 记录错误日志，或采取其他处理

    async def send_prompt(self, prompt):
        """
        prompt 格式：
        {
            "jilu_id": "task-001",  # 任务ID
            "uniqueid": "unique-task-id",  # 唯一标识符
            "prompt_data": {
                "cs_imgs": [
                    {
                        "upImage": "http://example.com/image.jpg",  # 图片URL
                        "node": 1  # 节点ID
                    }
                ],
                "cs_texts": [
                    {
                        "value": "示例文本",
                        "node": 2  # 节点ID
                    }
                ]
            }
        }
        """
        # 发送 prompt 消息给客户端
        prompt_message = {
            "type": "prompt",
            "data": prompt
        }
        await self.send(json.dumps(prompt_message))

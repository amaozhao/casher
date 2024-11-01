import json
import urllib.parse

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from task.models import UserTask

# from django.core.cache import cache


client_dict = {}
channel_dict = {}


class ClientConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # 解析查询参数，提取 clientId
        query_string = self.scope["query_string"].decode("utf-8")
        client_id = await self._get_client_id(query_string)

        if client_id:
            client_dict[client_id] = self.channel_name
            channel_dict[self.channel_name] = client_id
        await self.accept()

    async def _get_client_id(self, query_string):
        # 解析 clientId（如果存在）
        query_params = urllib.parse.parse_qs(query_string)
        return query_params.get("clientId", [None])[0]

    async def disconnect(self, close_code):
        client = channel_dict.get(self.channel_name)
        client_dict.pop(client, None)
        channel_dict.pop(self.channel_name, None)

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            message_type = data.get("type")

            # 处理来自客户端的 bind 消息
            if message_type == "crystools.bind":
                await self.handle_bind(data)
            elif message_type == "crystools.monitor":
                await self.handle_monitor(data)
            # 移除对 "prompt" 消息的处理，因为这是服务端发给客户端的消息
            elif message_type == "crystools.prompt_error":
                await self.handle_prompt_error(data)
            elif message_type == "crystools.prompt_ok":
                await self.handle_prompt_ok(data)
            elif message_type == "status":
                print("executed")
            elif message_type == "execution_start":
                print("executed")
            elif message_type == "executing":
                print("executed")
            elif message_type == "execution_error":
                print("execution_error")
            elif message_type == "executed":
                print("executed")
            elif message_type == "progress":
                print("execution_error")
            elif message_type == "execution_cached":
                print("executed")
            else:
                pass
        except Exception as e:
            print(f"Error processing message: {e}")

    async def handle_bind(self, data):
        client_id = data["data"]["client_id"]
        client_dict[client_id] = self.channel_name
        channel_dict[self.channel_name] = client_id
        print(f"Received bind message from client: {client_id}")

    async def handle_prompt_error(self, data):
        # 处理 prompt_error 消息
        jilu_id = data["data"]["jilu_id"]
        error_message = data["data"]["msg"]
        print(f"Received prompt_error message for task {jilu_id}: {error_message}")
        # 记录错误日志，或采取其他处理

    async def handle_monitor(self, data):
        client_id = data["data"]["client_id"]
        # cache.set(client_id, self.channel_name)
        channel_dict[self.channel_name] = client_id

    async def prompt(self, data):
        await self.send(json.dumps(data))

    async def handle_prompt(self, data):
        try:
            jilu_id = data["data"]["jilu_id"]
            print(f"Handling prompt for task {jilu_id}")
            # 添加你需要的业务逻辑
        except KeyError as e:
            print(f"Missing expected data in prompt message: {e}")
        except Exception as e:
            print(f"Error handling prompt message: {e}")

    async def handle_prompt_ok(self, data):
        try:
            jilu_id = data["data"]["jilu_id"]
            prompt_id = data["data"]["prompt_id"]
            await self.update_user_task(jilu_id, prompt_id)
            print(f"Handling prompt ok for task {jilu_id} with {prompt_id}")
            # 添加你需要的业务逻辑
        except KeyError as e:
            print(f"Missing expected data in prompt message: {e}")
        except Exception as e:
            print(f"Error handling prompt message: {e}")

    @database_sync_to_async
    def update_user_task(self, jilu_id, prompt_id):
        user_task = UserTask.objects.filter(jilu_id=jilu_id).first()
        if user_task:
            user_task.prompt_id = prompt_id
            user_task.save()

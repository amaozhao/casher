import json
import time
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer


class Consumer(AsyncWebsocketConsumer):

    async def connect(self):
        # 获取从 URL 传递的 client_id
        self.client_id = self.scope['url_route']['kwargs']['client_id']
        self.is_fu_connection = self.client_id.endswith("_fu")  # 判断是否为 _fu 连接

        # 接受 WebSocket 连接
        await self.accept()

        # 根据是否是 _fu 连接发送不同的绑定消息
        await self.send(json.dumps({
            "type": "crystools.bind",
            "data": {
                "client_id": self.client_id
            }
        }))

        # 如果是 _fu 连接，启动定期任务和队列任务处理
        if self.is_fu_connection:
            self.loop_num = 0
            self.websocket_queue = asyncio.Queue()  # 模拟 websocket_queue
            self.task = asyncio.create_task(self.send_heartbeat_and_process_queue())
        else:
            # 启动心跳包任务，非_fu连接按常规逻辑处理
            self.task = asyncio.create_task(self.send_heartbeat())

    async def receive(self, text_data):
        # 处理收到的 WebSocket 消息
        message = json.loads(text_data)
        message_type = message.get('type')

        if message_type == "executed":
            # 任务成功，发送确认
            await self.send(json.dumps({
                "type": "crystools.prompt_ok",
                "data": {
                    "prompt_id": message['data']['prompt_id'],
                    "jilu_id": message['data'].get('jilu_id', ''),
                    "msg": "发送指令成功"
                }
            }))
        elif message_type == "execution_error":
            # 任务出错，发送错误消息
            await self.send(json.dumps({
                "type": "crystools.prompt_error",
                "data": {
                    "jilu_id": message['data'].get('jilu_id', ''),
                    "msg": "任务执行出错"
                }
            }))
        elif message_type == "queue":
            # 处理队列信息
            await self.send(json.dumps({
                "type": "crystools.queue",
                "data": {
                    "client_id": self.client_id,
                    "queue_remaining": message['data'].get('queue_remaining', 0)
                }
            }))

    async def send_heartbeat(self):
        # 定期发送心跳包（非 _fu 连接）
        while True:
            await asyncio.sleep(10)  # 每 10 秒发送一次心跳包
            await self.send(json.dumps({
                "type": "crystools.monitor",
                "data": {
                    "files": ["file1.json", "file2.json"],
                    "running": ["task1"],
                    "pending": ["task2", "task3"],
                    "client_id": self.client_id
                }
            }))

    async def send_heartbeat_and_process_queue(self):
        # _fu 连接专用：定期发送心跳包并处理 websocket_queue
        while True:
            try:
                if not self.websocket_queue.empty():
                    websocket_info = await self.websocket_queue.get()
                    if "conn_identifier" in websocket_info:
                        websocket_info["data"]["zhu_client_id"] = self.client_id
                        if websocket_info["conn_identifier"] == 1:
                            await self.send(json.dumps(websocket_info["data"]))
                else:
                    self.loop_num += 1
                    if self.loop_num > 100:
                        self.loop_num = 0
                        await self.send(json.dumps({
                            "time": self.get_time(),
                        }))
            except Exception as e:
                break
            finally:
                await asyncio.sleep(0.02)

    async def disconnect(self, close_code):
        # 处理 WebSocket 断开，取消任务
        if hasattr(self, 'task'):
            self.task.cancel()
        pass

    def get_time(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

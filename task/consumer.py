import json
import urllib.parse

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from payment.models import UserHashrate
from task.models import TaskFreeCount, UserTask
from wxappb.models import AuthorTechs
from payment.models import UserPayin
from invitation.models import InvitationRelation
from cash_statistics.tasker import update_statistics
from django.conf import settings
import logging

# 获取 channels 的 logger
logger = logging.getLogger('channel')


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
            logger.info(f'connect client_id: {client_id}, wss: {self.channel_name}')
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
                logger.info("executed")
            elif message_type == "execution_start":
                logger.info("execution start")
            elif message_type == "executing":
                logger.info("executing")
            elif message_type == "execution_error":
                logger.info("execution_error")
            elif message_type == "executed":
                logger.info("executed")
            elif message_type == "progress":
                logger.info("progress")
            elif message_type == "execution_cached":
                logger.info("execution_cached")
            else:
                pass
        except Exception as e:
            print(f"Error processing message: {e}")

    async def handle_bind(self, data):
        client_id = data["data"]["client_id"]
        client_dict[client_id] = self.channel_name
        channel_dict[self.channel_name] = client_id
        logger.info(f"Received bind message from client: {client_id}")

    async def handle_prompt_error(self, data):
        # 处理 prompt_error 消息
        jilu_id = data["data"]["jilu_id"]
        prompt_id = data["data"]["prompt_id"]
        error_message = data["data"]["msg"]
        logger.info(f"Received prompt_error message for task {jilu_id}: {error_message}")
        # 记录错误日志，或采取其他处理

    async def handle_monitor(self, data):
        client_id = data["data"]["client_id"]
        channel_dict[self.channel_name] = client_id

    async def handle_prompt_ok(self, data):
        try:
            jilu_id = data["data"]["jilu_id"]
            prompt_id = data["data"]["prompt_id"]
            await self.update_user_success_task(jilu_id, prompt_id)
            logger.info(f"Handling prompt ok for task {jilu_id} with {prompt_id}")
        except KeyError as e:
            logger.info(f"Missing expected data in prompt message: {e}")
        except Exception as e:
            logger.info(f"Error handling prompt message: {e}")

    @database_sync_to_async
    def update_user_success_task(self, jilu_id, prompt_id, is_ok=True):
        user_task = UserTask.objects.filter(jilu_id=jilu_id).first()
        if user_task:
            user_task.prompt_id = prompt_id
            if is_ok:
                user_task.status = 'success'
            else:
                user_task.status = 'failed'
            user_task.save()
            user_hashrate = UserHashrate.objects.filter(user=user_task.user).first()
            task_free_count = TaskFreeCount.objects.filter(
                workflow=user_task.flow
            ).first()
            is_free = task_free_count.free_count < user_task.flow.free_times
            if is_free:
                task_free_count.free_count += 1
                task_free_count.save()
                return
            if user_hashrate:
                if is_ok:
                    user_hashrate.hashrate -= user_task.fee
                    user_hashrate.save()
            self.update_pay(user_task, is_free)
            update_statistics.delay_on_commit(user_task.user.id)

    @database_sync_to_async
    def update_error_task(self, jilu_id, prompt_id):
        user_task = UserTask.objects.filter(jilu_id=jilu_id).first()
        if user_task:
            user_task.prompt_id = prompt_id
            user_task.status = 'failed'
            user_task.save()
            task_free_count = TaskFreeCount.objects.filter(
                workflow=user_task.flow
            ).first()
            is_free = task_free_count.free_count < user_task.flow.free_times
            if is_free:
                task_free_count.free_count += 1
                task_free_count.save()
                return
            self.update_pay(user_task, is_free, is_success=False)

    def update_pay(self, user_task, is_free, is_success=True):
        workflow = user_task.flow
        fee = 0.0
        if not is_free:
            if is_success:
                fee = workflow.fee * 0.7
        tech = AuthorTechs.objects.filter(techsid=workflow.techsid).first()
        if tech:
            author = tech.user
            UserPayin.objects.create(
                user=author,
                workflow=workflow,
                fee=fee,
                status='failed'
            )
            invite = InvitationRelation.objects.filter(invitee=author).first()
            if invite:
                author = invite.inviter
                UserPayin.objects.create(
                    user=author,
                    workflow=workflow,
                    fee=workflow.fee * 0.1,
                    status='failed'
                )

import pytest
from channels.testing import WebsocketCommunicator
from casher.asgi import application


@pytest.mark.asyncio
async def test_websocket_connect():
    # 测试普通 WebSocket 连接
    client_id = "test-client-id"
    communicator = WebsocketCommunicator(application, f"/ws/server1/{client_id}/")

    connected, subprotocol = await communicator.connect()
    assert connected

    # 接收绑定消息，确认连接成功
    response = await communicator.receive_json_from()
    assert response == {
        "type": "crystools.bind",
        "data": {
            "client_id": client_id
        }
    }

    await communicator.disconnect()


@pytest.mark.asyncio
async def test_websocket_fu_connect():
    # 测试 _fu 连接的绑定和初始化
    client_id = "test-client-id_fu"
    communicator = WebsocketCommunicator(application, f"/ws/server1/{client_id}/")

    connected, subprotocol = await communicator.connect()
    assert connected

    # 接收绑定消息，确认 _fu 连接成功
    response = await communicator.receive_json_from()
    assert response == {
        "type": "crystools.bind",
        "data": {
            "client_id": client_id
        }
    }

    await communicator.disconnect()


@pytest.mark.asyncio
async def test_task_executed():
    # 测试普通 WebSocket 任务执行成功后的交互
    client_id = "test-client-id"
    communicator = WebsocketCommunicator(application, f"/ws/server1/{client_id}/")

    connected, subprotocol = await communicator.connect()
    assert connected

    # 模拟任务执行完成后的返回消息
    executed_message = {
        "type": "executed",
        "data": {
            "prompt_id": "test-prompt-id",
            "jilu_id": "test-jilu-id"
        }
    }

    await communicator.send_json_to(executed_message)
    response = await communicator.receive_json_from()
    assert response == {
        "type": "crystools.prompt_ok",
        "data": {
            "prompt_id": "test-prompt-id",
            "jilu_id": "test-jilu-id",
            "msg": "发送指令成功"
        }
    }

    await communicator.disconnect()


@pytest.mark.asyncio
async def test_task_execution_error():
    # 测试普通 WebSocket 任务执行错误后的交互
    client_id = "test-client-id"
    communicator = WebsocketCommunicator(application, f"/ws/server1/{client_id}/")

    connected, subprotocol = await communicator.connect()
    assert connected

    # 模拟任务执行错误后的返回消息
    error_message = {
        "type": "execution_error",
        "data": {
            "prompt_id": "test-prompt-id",
            "jilu_id": "test-jilu-id"
        }
    }

    await communicator.send_json_to(error_message)
    response = await communicator.receive_json_from()
    assert response == {
        "type": "crystools.prompt_error",
        "data": {
            "jilu_id": "test-jilu-id",
            "msg": "任务执行出错"
        }
    }

    await communicator.disconnect()


@pytest.mark.asyncio
async def test_queue_status_update():
    # 测试普通 WebSocket 队列状态更新的交互
    client_id = "test-client-id"
    communicator = WebsocketCommunicator(application, f"/ws/server1/{client_id}/")

    connected, subprotocol = await communicator.connect()
    assert connected

    # 模拟队列状态更新消息
    queue_message = {
        "type": "queue",
        "data": {
            "queue_remaining": 5
        }
    }

    await communicator.send_json_to(queue_message)
    response = await communicator.receive_json_from()
    assert response == {
        "type": "crystools.queue",
        "data": {
            "client_id": client_id,
            "queue_remaining": 5
        }
    }

    await communicator.disconnect()


@pytest.mark.asyncio
async def test_fu_task_queue_processing():
    # 测试 _fu 连接的任务队列处理
    client_id = "test-client-id_fu"
    communicator = WebsocketCommunicator(application, f"/ws/server1/{client_id}/")

    connected, subprotocol = await communicator.connect()
    assert connected

    # 模拟向 websocket_queue 发送任务
    task_message = {
        "type": "task",
        "data": {
            "task_id": "123",
            "conn_identifier": 1
        }
    }

    await communicator.send_json_to(task_message)
    # 等待接收队列处理的反馈
    response = await communicator.receive_json_from()
    assert response == {
        "type": "task_processed",
        "data": {
            "task_id": "123",
            "status": "success"
        }
    }

    await communicator.disconnect()


@pytest.mark.asyncio
async def test_send_heartbeat():
    # 测试普通 WebSocket 连接的心跳包
    client_id = "test-client-id"
    communicator = WebsocketCommunicator(application, f"/ws/server1/{client_id}/")

    connected, subprotocol = await communicator.connect()
    assert connected

    # 模拟心跳包返回的状态
    response = await communicator.receive_json_from()
    assert response == {
        "type": "crystools.monitor",
        "data": {
            "files": ["file1.json", "file2.json"],
            "running": ["task1"],
            "pending": ["task2", "task3"],
            "client_id": client_id
        }
    }

    await communicator.disconnect()


@pytest.mark.asyncio
async def test_fu_heartbeat_and_time():
    # 测试 _fu 连接的心跳包和时间发送
    client_id = "test-client-id_fu"
    communicator = WebsocketCommunicator(application, f"/ws/server1/{client_id}/")

    connected, subprotocol = await communicator.connect()
    assert connected

    # 模拟心跳包返回的状态
    response = await communicator.receive_json_from()
    assert response == {
        "type": "crystools.monitor",
        "data": {
            "files": ["file1.json", "file2.json"],
            "running": ["task1"],
            "pending": ["task2", "task3"],
            "client_id": client_id
        }
    }

    # 等待定时发送的时间信息
    time_response = await communicator.receive_json_from()
    assert "time" in time_response

    await communicator.disconnect()

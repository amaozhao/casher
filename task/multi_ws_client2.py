import asyncio
import json

import websockets

# WebSocket连接的URL
ws_url = "ws://localhost:8000/ws"

# 要发送的初始消息模板
initial_message_template = {"type": "crystools.bind", "data": {"client_id": ""}}


# 创建单个WebSocket连接并发送初始消息
async def connect_and_send(client_id):
    async with websockets.connect(ws_url) as websocket:
        # 设置client_id
        initial_message = initial_message_template.copy()
        initial_message["data"]["client_id"] = client_id

        # 发送消息
        await websocket.send(json.dumps(initial_message))
        print(f"Sent message to client {client_id}: {initial_message}")

        # 等待服务器的响应
        response = await websocket.recv()
        print(f"Received message from server for client {client_id}: {response}")


# 创建3个WebSocket连接
async def main():
    # 定义3个客户端ID
    client_ids = ["a", "b", "c"]

    # 创建3个任务
    tasks = [connect_and_send(client_id) for client_id in client_ids]

    # 等待所有任务完成
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    # 运行脚本
    asyncio.run(main())

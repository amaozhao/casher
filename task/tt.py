import asyncio
import websockets
import json
import uuid

# 初始 WebSocket 服务地址（不带 clientId）
initial_ws_uri = "ws://localhost:8000/ws/"

async def receive_messages(websocket):
    while True:
        try:
            # 等待接收消息
            message = await websocket.recv()
            message_data = json.loads(message)
            message_type = message_data.get('type')

            if message_type == "init":
                # 收到 init 消息，提取 clientId
                client_id = message_data['data']['client_id']
                print(f"Received init message with client_id: {client_id}")
                return client_id  # 返回 client_id，并结束循环

            elif message_type == "prompt":
                # 处理 prompt 消息
                print(f"Received prompt message: {message_data['data']}")
                await process_prompt(message_data['data'])

            elif message_type == "test_prompt":
                # 处理 test_prompt 消息
                print(f"Received test_prompt message: {message_data['data']}")
                return message_data['data']  # 返回数据，继续等待其他消息

        except websockets.exceptions.ConnectionClosed:
            print("Connection closed")
            break

async def process_prompt(data):
    # 模拟处理 prompt 数据
    jilu_id = data.get('jilu_id')
    uniqueid = data.get('uniqueid')
    print(f"Processing prompt task {jilu_id} with uniqueid {uniqueid}")

    # 处理图像
    cs_imgs = data['prompt_data'].get('cs_imgs', [])
    for img in cs_imgs:
        image_url = img['upImage']
        node = img['node']
        print(f"Downloading image from {image_url} for node {node}")

    # 处理文本
    cs_texts = data['prompt_data'].get('cs_texts', [])
    for text in cs_texts:
        text_value = text['value']
        node = text['node']
        print(f"Processing text '{text_value}' for node {node}")

async def main():
    # 第一步：连接初始 WebSocket 服务并发送 bind 消息
    async with websockets.connect(initial_ws_uri) as websocket:
        print(f"Connected to server: {initial_ws_uri}")

        # 生成 client_id
        generated_client_id = str(uuid.uuid4())
        print(f"Generated client_id: {generated_client_id}")

        # 发送 bind 消息
        bind_message = {
            "type": "crystools.bind",
            "data": {
                "client_id": generated_client_id  # 模拟生成的 clientId
            }
        }
        await websocket.send(json.dumps(bind_message))
        print("Sent bind message to server")

        # 等待服务端返回 init 消息，提取 clientId
        client_id = await receive_messages(websocket)

    # 第二步：带上 clientId 连接新的 WebSocket 服务
    ws_uri_with_clientid = f"ws://localhost:8000/ws/?clientId={client_id}"
    async with websockets.connect(ws_uri_with_clientid) as websocket:
        bind_message = {
            "type": "crystools.bind",
            "data": {
                "client_id": generated_client_id  # 模拟生成的 clientId
            }
        }
        await websocket.send(json.dumps(bind_message))
        bind_message = {
            "type": "crystools.test_prompt",
            "data": {
                "client_id": generated_client_id  # 模拟生成的 clientId
            }
        }
        await websocket.send(json.dumps(bind_message))
        await receive_messages(websocket)
        await receive_messages(websocket)


if __name__ == '__main__':
    # 运行测试
    asyncio.get_event_loop().run_until_complete(main())

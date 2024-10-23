import asyncio
import websockets
import json

# WebSocket server address (replace with your server's WebSocket address)
WEBSOCKET_URL = "ws://192.168.10.106:8000/ws"

# The prompt message to be sent
prompt_message = {
    "message_type": "prompt",
    "uniqueid": "12345abcd",
    "data": {
        "jilu_id": "67890xyz",
        "cs_imgs": [
            {
                "upImage": "http://192.168.10.106:8000/media/user/images/%E7%BE%8E%E5%A5%B3_bTPFqQR.png",
                "node": "29",
            }
        ],
        "cs_videos": [],
        "cs_texts": [{"node": "4", "value": "This is a sample text for node 4."}],
    },
}


async def send_prompt_message():
    async with websockets.connect(WEBSOCKET_URL) as websocket:
        # Send the prompt message as JSON
        await websocket.send(json.dumps(prompt_message))
        print(f"Sent: {json.dumps(prompt_message)}")

        # Wait to receive a response from the server
        response = await websocket.recv()
        print(f"Received: {response}")


if __name__ == "__main__":
    # Run the test
    asyncio.get_event_loop().run_until_complete(send_prompt_message())

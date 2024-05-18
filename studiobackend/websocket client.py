import asyncio
import websockets
import json


async def receive_messages():
    uri = "ws://localhost:8000/ws/crewai/"

    async with websockets.connect(uri) as websocket:
        print("Connected to server")

        # Send an initial message to the server
        await websocket.send(json.dumps({"input": "What kind of marketing job should I pursue"}))
        print("Message sent to server")

        try:
            while True:
                # Receive message from the server
                message = await websocket.recv()
                print(f"Raw message received: {message}")
                data = json.loads(message)
                print(f"Parsed message: {data}")
        except websockets.ConnectionClosed:
            print("Connection closed")


asyncio.get_event_loop().run_until_complete(receive_messages())

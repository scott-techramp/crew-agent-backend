import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .crewai import process_stream
import asyncio
import logging

class CrewAIConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        user_input = text_data_json['input']

        async for step in process_stream(user_input):
            print("ASYNC Consumer Step: ", step)
            await self.send(text_data=json.dumps(step))
            print(f"Sent step: {step}")

        print("ASYNC process_stream Done... closing websocket.")
        await self.close()
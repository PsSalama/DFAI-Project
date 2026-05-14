import json
import asyncio
from config.async_redis import async_redis_client
from src.memoryHandling.app.services.process.process_handling_file_service import ProcessHandlingFileService


class TaskListener:
    def __init__(
        self,
        process_handling_file_service: ProcessHandlingFileService
    ):
        self.process_handling_file_service = (
            process_handling_file_service
        )


    async def listen(self):
        pubsub = async_redis_client.pubsub()
        await pubsub.subscribe(
            "task_process_events"
        )
        print(
            "Listening for task events..."
        )
        async for message in pubsub.listen():
            print("RAW MESSAGE:", message)
            if message["type"] != "message":
                continue
            data = json.loads(
                message["data"]
            )
            await self.handle_event(data)


    async def handle_event(
        self,
        data: dict
    ):
        event = data.get("event")
        print(f"Received event: {event}")
        if event == "PROCESS_COMPLETED":
            await self.on_process_extraction_completed(
                data
            )


    async def on_process_extraction_completed(
        self,
        data: dict
    ):
        output_file = data["output_file"]
        parsed_data = await asyncio.to_thread(
            self.process_handling_file_service.parse_process_file,
            output_file
        )
        stored_data = await asyncio.to_thread(
            self.process_handling_file_service.store_data,
            parsed_data
        )
        print(
            f"Stored {len(stored_data)} processes"
        )
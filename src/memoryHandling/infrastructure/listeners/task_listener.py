import json
from config.redis import redis_client
from services.process.process_handling_file_service import ProcessHandlingFileService


class TaskListener:
    def __init__(self, process_handling_file_service: ProcessHandlingFileService):
        self.process_handling_file_service = process_handling_file_service


    # Listen on Specific Channel
    async def listen(self):
        pubsub = redis_client.pubsub()
        await pubsub.subscribe(
            "task_process_events"
        )
        print("Listening for task events...")
        async for message in pubsub.listen():
            if message["type"] != "message":
                continue
            data = json.loads(
                message["data"]
            )
            await self.handle_event(data)


    # Handle Specific Event
    async def handle_event(self, data: dict):
        event = data["event"]
        if event == "PROCESS_COMPLETED":
            await self.on_process_extraction_completed(
                data
            )


    async def on_process_extraction_completed(self, data: dict):
        output_file = data["output_file"]
        await self.process_handling_file_service.parse_process_file(output_file)
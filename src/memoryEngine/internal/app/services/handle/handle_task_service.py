from src.memoryEngine.internal.app.ports.handle.i_handle_task_producer import IHandleTaskProducer
from src.memoryEngine.internal.app.dto.task_request import TaskRequest


class HandleTaskService:
    def __init__(self, producer: IHandleTaskProducer):
        self.producer = producer


    async def all_tasks(self, file_path: str) -> dict:
        await self.handle_task(file_path)
        return {
            "request_status": "success"
        }


    async def handle_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "handle_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.handles"
            }
        )
        return await self.producer.handle_task(new_task)
from src.memoryEngine.internal.app.ports.memory.i_memory_task_producer import IMemoryTaskProducer
from src.memoryEngine.internal.app.dto.task_request import TaskRequest


class MemoryTaskService:
    def __init__(self, producer: IMemoryTaskProducer) -> None:
        self.producer = producer


    async def all_tasks(self, file_path: str) -> dict:
        await self.memory_info_task(file_path)
        return {
            "request_status": "success"
        }


    async def memory_info_task(self, file_path: str) -> list[dict]:
        new_task = TaskRequest(
            task_name = "memory_info_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.info"
            }
        )
        return await self.producer.memory_info_task(new_task)
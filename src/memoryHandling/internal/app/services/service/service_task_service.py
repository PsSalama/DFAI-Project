import asyncio
from src.memoryHandling.internal.app.ports.service.i_service_task_producer import IServiceTaskProducer
from src.memoryHandling.internal.app.dto.task_request import TaskRequest


class ServiceTaskService:
    def __init__(self, producer: IServiceTaskProducer) -> None:
        self.producer = producer

    async def all_tasks(self, file_path: str):
        await asyncio.gather(
            self.service_scan_task(file_path),
        )


    async def service_scan_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "service_scan_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.svcscan"
            }
        )
        return await self.producer.service_scan_task(new_task)
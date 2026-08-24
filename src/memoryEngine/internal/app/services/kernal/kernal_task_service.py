from src.memoryEngine.internal.app.ports.kernal.i_kernal_task_producer import IKernalTaskProducer
from src.memoryEngine.internal.app.dto.task_request import TaskRequest


class KernalTaskService:
    def __init__(self, producer: IKernalTaskProducer):
        self.producer = producer


    async def all_tasks(self, file_path: str) -> dict:
        await self.ssdt_task(file_path)
        return {
            "request_status": "success"
        }


    async def ssdt_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "ssdt_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.ssdt"
            }
        )
        return await self.producer.ssdt_task(new_task)
from src.memoryHandling.app.ports.process.i_process_task_producer import IProcessTaskProducer
from src.memoryHandling.app.dto.task_request import TaskRequest


class ProcessTaskService:
    def __init__(self, producer: IProcessTaskProducer):
        self.producer = producer


    async def all_tasks(self, file_path: str) -> dict:
        await self.process_list_task(file_path)
        return {
            "request_status": "success"
        }


    async def process_list_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "process_list_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.psxview"
            }
        )
        return await self.producer.process_list_task(new_task)
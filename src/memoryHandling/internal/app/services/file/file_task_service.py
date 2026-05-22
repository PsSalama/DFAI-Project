from src.memoryHandling.internal.app.ports.file.i_file_task_producer import IFileTaskProducer
from src.memoryHandling.internal.app.dto.task_request import TaskRequest


class FileTaskService:
    def __init__(self, producer: IFileTaskProducer):
        self.producer = producer


    async def all_tasks(self, file_path: str) -> dict:
        await self.file_scan_task(file_path)
        await self.file_dump_task(file_path)
        return {
            "request_status": "success"
        }


    async def file_scan_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "file_scan_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.filescan"
            }
        )
        return await self.producer.file_scan_task(new_task)


    async def file_dump_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "file_dump_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.dumpfiles"
            }
        )
        return await self.producer.file_dump_task(new_task)


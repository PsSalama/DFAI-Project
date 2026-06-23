from src.memoryEngine.internal.app.ports.process.i_process_task_producer import IProcessTaskProducer
from src.memoryEngine.internal.app.dto.task_request import TaskRequest


class ProcessTaskService:
    def __init__(self, producer: IProcessTaskProducer):
        self.producer = producer


    async def all_tasks(self, file_path: str) -> dict:
        await self.process_view_task(file_path)
        await self.process_list_task(file_path)
        await self.process_scan_task(file_path)
        await self.process_tree_task(file_path)
        return {
            "request_status": "success"
        }


    async def process_view_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "process_view_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.psxview"
            }
        )
        return await self.producer.process_view_task(new_task)


    async def process_list_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "process_list_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.pslist"
            }
        )
        return await self.producer.process_list_task(new_task)


    async def process_scan_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "process_scan_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.psscan"
            }
        )
        return await self.producer.process_scan_task(new_task)


    async def process_tree_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "process_tree_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.pstree"
            }
        )
        return await self.producer.process_tree_task(new_task)

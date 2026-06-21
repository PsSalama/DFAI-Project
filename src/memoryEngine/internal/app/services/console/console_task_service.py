from src.memoryEngine.internal.app.ports.console.i_console_task_producer import IConsoleTaskProducer
from src.memoryEngine.internal.app.dto.task_request import TaskRequest


class ConsoleTaskService:
    def __init__(self, producer: IConsoleTaskProducer):
        self.producer = producer


    async def all_tasks(self, file_path: str) -> dict:
        await self.console_task(file_path)
        await self.console_cmdscan_task(file_path)
        return {
            "request_status": "success"
        }


    async def console_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "console_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.console"
            }
        )
        return await self.producer.console_task(new_task)


    async def console_cmdscan_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "console_cmdscan_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.cmdscan"
            }
        )
        return await self.producer.console_cmdscan_task(new_task)
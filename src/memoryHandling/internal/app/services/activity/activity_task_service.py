from src.memoryHandling.internal.app.ports.activity.i_activity_task_producer import IActivityTaskProducer
from src.memoryHandling.internal.app.dto.task_request import TaskRequest


class ActivityTaskService:
    def __init__(self, producer: IActivityTaskProducer):
        self.producer = producer


    async def all_tasks(self, file_path: str) -> dict:
        await self.activity_session_task(file_path)
        await self.activity_sid_task(file_path)
        await self.activity_desktop_task(file_path)
        return {
            "request_status": "success"
        }


    async def activity_session_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "activity_session_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.sessions"
            }
        )
        return await self.producer.activity_session_task(new_task)


    async def activity_sid_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "activity_sid_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.getsids"
            }
        )
        return await self.producer.activity_sid_task(new_task)


    async def activity_desktop_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "activity_desktop_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.desktops"
            }
        )
        return await self.producer.activity_desktop_task(new_task)
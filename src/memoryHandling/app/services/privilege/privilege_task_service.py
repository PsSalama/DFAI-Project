import asyncio
from src.memoryHandling.app.ports.privilege.i_privilege_task_producer import IPrivilegeTaskProducer
from src.memoryHandling.app.dto.task_request import TaskRequest


class PrivilegeTaskService:
    def __init__(self, producer: IPrivilegeTaskProducer):
        self.producer = producer

    async def all_tasks(self, file_path: str):
        await asyncio.gather(
            self.privilege_process_task(file_path),
            self.privilege_service_id_task(file_path)
        )


    async def privilege_process_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "privilege_process_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.privileges"
            }
        )
        return await self.producer.privilege_process_task(new_task)


    async def privilege_service_id_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "privilege_service_id_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.getservicesids"
            }
        )
        return await self.producer.privilege_service_id_task(new_task)
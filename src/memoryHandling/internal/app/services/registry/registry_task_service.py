import asyncio
from src.memoryHandling.internal.app.ports.registry.i_registry_task_producer import IRegistryTaskProducer
from src.memoryHandling.internal.app.dto.task_request import TaskRequest


class RegistryTaskService:
    def __init__(self, producer: IRegistryTaskProducer):
        self.producer = producer

    async def all_tasks(self, file_path: str):
        await asyncio.gather(
            self.registry_list_task(file_path),
            self.registry_scan_task(file_path),
            self.registry_key_task(file_path),
            self.registry_cert_task(file_path),
        )


    async def registry_list_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "registry_list_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.registry.hivelist"
            }
        )
        return await self.producer.registry_list_task(new_task)


    async def registry_scan_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "registry_scan_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.registry.hivescan"
            }
        )
        return await self.producer.registry_scan_task(new_task)


    async def registry_key_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "registry_key_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.registry.printkey"
            }
        )
        return await self.producer.registry_key_task(new_task)


    async def registry_cert_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "registry_cert_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.registry.certificates"
            }
        )
        return await self.producer.registry_cert_task(new_task)
from src.memoryHandling.internal.app.ports.dll.i_dll_task_producer import IDllTaskProducer
from src.memoryHandling.internal.app.dto.task_request import TaskRequest


class DllTaskService:
    def __init__(self, producer: IDllTaskProducer):
        self.producer = producer


    async def all_tasks(self, file_path: str) -> dict:
        await self.dll_list_task(file_path)
        await self.dll_ldrmodules_task(file_path)
        await self.dll_module_task(file_path)
        await self.dll_modscan_task(file_path)
        return {
            "request_status": "success"
        }


    async def dll_list_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "dll_list_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.dlllist"
            }
        )
        return await self.producer.dll_list_task(new_task)


    async def dll_ldrmodules_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "dll_ldrmodules_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.ldrmodules"
            }
        )
        return await self.producer.dll_ldrmodules_task(new_task)


    async def dll_module_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "dll_module_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.modules"
            }
        )
        return await self.producer.dll_module_task(new_task)


    async def dll_modscan_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "dll_modscan_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.modscan"
            }
        )
        return await self.producer.dll_modscan_task(new_task)
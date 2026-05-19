from src.memoryHandling.app.services.process.process_task_service import ProcessTaskService
from src.memoryHandling.app.services.registry.process_task_service import RegistryTaskService
from src.memoryHandling.app.services.dll.dll_task_service import DllTaskService
from src.memoryHandling.app.services.activity.activity_task_service import ActivityTaskService
from src.memoryHandling.app.services.privilege.privilege_task_service import PrivilegeTaskService


class MainService:
    def __init__(
            self,
            process_task_service: ProcessTaskService,
            registry_task_service: RegistryTaskService,
            dll_task_service: DllTaskService,
            activity_task_service: ActivityTaskService,
            privilege_task_service: PrivilegeTaskService
    ):
        self.process_task_service = process_task_service
        self.registry_task_service = registry_task_service
        self.dll_task_service = dll_task_service
        self.activity_task_service = activity_task_service
        self.privilege_task_service = privilege_task_service


    async def main_tasks(self, file_path: str) -> dict:
        await self.process_task_service.all_tasks(file_path)
        await self.registry_task_service.all_tasks(file_path)
        await self.dll_task_service.dll_tasks(file_path)
        await self.activity_task_service.dll_tasks(file_path)
        await self.privilege_task_service.all_tasks(file_path)
        return {
            "status": "success",
            "message": "All tasks dispatched successfully"
        }
from src.memoryHandling.internal.app.services.process.process_task_service import ProcessTaskService
from src.memoryHandling.internal.app.services.registry.registry_task_service import RegistryTaskService
from src.memoryHandling.internal.app.services.dll.dll_task_service import DllTaskService
from src.memoryHandling.internal.app.services.activity.activity_task_service import ActivityTaskService
from src.memoryHandling.internal.app.services.privilege.privilege_task_service import PrivilegeTaskService
from src.memoryHandling.internal.app.services.file.file_task_service import FileTaskService
from src.memoryHandling.internal.app.services.service.service_task_service import ServiceTaskService
from src.memoryHandling.internal.app.services.driver.driver_task_service import DriverTaskService
from src.memoryHandling.internal.app.services.memory.memory_task_service import MemoryTaskService


class MainService:
    def __init__(
            self,
            process_task_service: ProcessTaskService,
            registry_task_service: RegistryTaskService,
            dll_task_service: DllTaskService,
            activity_task_service: ActivityTaskService,
            privilege_task_service: PrivilegeTaskService,
            file_task_service: FileTaskService,
            service_task_service: ServiceTaskService,
            driver_task_service: DriverTaskService,
            memory_task_service: MemoryTaskService,
    ):
        self.process_task_service = process_task_service
        self.registry_task_service = registry_task_service
        self.dll_task_service = dll_task_service
        self.activity_task_service = activity_task_service
        self.privilege_task_service = privilege_task_service
        self.file_task_service = file_task_service
        self.service_task_service = service_task_service
        self.driver_task_service = driver_task_service
        self.memory_task_service = memory_task_service


    async def main_tasks(self, file_path: str) -> dict:
        await self.process_task_service.all_tasks(file_path)
        await self.registry_task_service.all_tasks(file_path)
        await self.dll_task_service.dll_tasks(file_path)
        await self.activity_task_service.dll_tasks(file_path)
        await self.privilege_task_service.all_tasks(file_path)
        await self.file_task_service.all_tasks(file_path)
        await self.service_task_service.all_tasks(file_path)
        await self.driver_task_service.all_tasks(file_path)
        await self.memory_task_service.all_tasks(file_path)
        return {
            "status": "success",
            "message": "All tasks dispatched successfully"
        }
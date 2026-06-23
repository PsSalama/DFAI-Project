from src.memoryEngine.internal.app.services.process.process_task_service import ProcessTaskService
from src.memoryEngine.internal.app.services.registry.registry_task_service import RegistryTaskService
from src.memoryEngine.internal.app.services.dll.dll_task_service import DllTaskService
from src.memoryEngine.internal.app.services.activity.activity_task_service import ActivityTaskService
from src.memoryEngine.internal.app.services.privilege.privilege_task_service import PrivilegeTaskService
from src.memoryEngine.internal.app.services.file.file_task_service import FileTaskService
from src.memoryEngine.internal.app.services.service.service_task_service import ServiceTaskService
from src.memoryEngine.internal.app.services.driver.driver_task_service import DriverTaskService
from src.memoryEngine.internal.app.services.memory.memory_task_service import MemoryTaskService
from src.memoryEngine.internal.app.services.network.network_task_service import NetworkTaskService
from src.memoryEngine.internal.app.services.console.console_task_service import ConsoleTaskService
from src.memoryEngine.internal.app.services.handle.handle_task_service import HandleTaskService


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
            network_task_service: NetworkTaskService,
            console_task_service: ConsoleTaskService,
            handle_task_service: HandleTaskService,
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
        self.network_task_service = network_task_service
        self.console_task_service = console_task_service
        self.handle_task_service = handle_task_service


    async def main_tasks(self, file_path: str) -> dict:
        await self.process_task_service.all_tasks(file_path)
        await self.registry_task_service.all_tasks(file_path)
        await self.dll_task_service.all_tasks(file_path)
        await self.activity_task_service.all_tasks(file_path)
        await self.privilege_task_service.all_tasks(file_path)
        await self.file_task_service.all_tasks(file_path)
        await self.service_task_service.all_tasks(file_path)
        await self.driver_task_service.all_tasks(file_path)
        await self.memory_task_service.all_tasks(file_path)
        await self.network_task_service.all_tasks(file_path)
        await self.console_task_service.all_tasks(file_path)
        await self.handle_task_service.all_tasks(file_path)
        return {
            "status": "success",
            "message": "All tasks dispatched successfully"
        }
from src.memoryEngine.internal.app.ports.process.i_process_task_producer import IProcessTaskProducer
from src.memoryEngine.internal.infrastructure.adapters.process.imp_process_task_producer import ImpProcessTaskProducer

from src.memoryEngine.internal.app.ports.process.i_process_repo import IProcessRepo
from src.memoryEngine.internal.infrastructure.adapters.process.imp_process_repo import ImpProcessRepo

from src.memoryEngine.internal.app.ports.registry.i_registry_task_producer import IRegistryTaskProducer
from src.memoryEngine.internal.infrastructure.adapters.registry.imp_registry_task_producer import ImpRegistryTaskProducer

from src.memoryEngine.internal.app.ports.registry.i_registry_repo import IRegistryRepo
from src.memoryEngine.internal.infrastructure.adapters.registry.imp_registry_repo import ImpRegistryRepo

from src.memoryEngine.internal.app.ports.dll.i_dll_task_producer import IDllTaskProducer
from src.memoryEngine.internal.infrastructure.adapters.dll.imp_dll_task_producer import ImpDllTaskProducer

from src.memoryEngine.internal.app.ports.dll.i_dll_repo import IDllRepo
from src.memoryEngine.internal.infrastructure.adapters.dll.imp_dll_repo import ImpDllRepo

from src.memoryEngine.internal.app.ports.activity.i_activity_task_producer import IActivityTaskProducer
from src.memoryEngine.internal.infrastructure.adapters.activity.imp_activity_task_producer import ImpActivityTaskProducer

from src.memoryEngine.internal.app.ports.activity.i_activity_repo import IActivityRepo
from src.memoryEngine.internal.infrastructure.adapters.activity.imp_activity_repo import ImpActivityRepo

from src.memoryEngine.internal.app.ports.privilege.i_privilege_task_producer import IPrivilegeTaskProducer
from src.memoryEngine.internal.infrastructure.adapters.privilege.imp_privilege_task_producer import ImpPrivilegeTaskProducer

from src.memoryEngine.internal.app.ports.privilege.i_privilege_repo import IPrivilegeRepo
from src.memoryEngine.internal.infrastructure.adapters.privilege.imp_privilege_repo import ImpPrivilegeRepo

from src.memoryEngine.internal.app.ports.file.i_file_task_producer import IFileTaskProducer
from src.memoryEngine.internal.infrastructure.adapters.file.imp_file_task_producer import ImpFileTaskProducer

from src.memoryEngine.internal.app.ports.file.i_file_repo import IFileRepo
from src.memoryEngine.internal.infrastructure.adapters.file.imp_file_repo import ImpFileRepo

from src.memoryEngine.internal.app.ports.service.i_service_task_producer import IServiceTaskProducer
from src.memoryEngine.internal.infrastructure.adapters.service.imp_service_task_producer import ImpServiceTaskProducer

from src.memoryEngine.internal.app.ports.service.i_service_repo import IServiceRepo
from src.memoryEngine.internal.infrastructure.adapters.service.imp_service_repo import ImpServiceRepo

from src.memoryEngine.internal.app.ports.driver.i_driver_task_producer import IDriverTaskProducer
from src.memoryEngine.internal.infrastructure.adapters.driver.imp_driver_task_producer import ImpDriverTaskProducer

from src.memoryEngine.internal.app.ports.driver.i_driver_repo import IDriverRepo
from src.memoryEngine.internal.infrastructure.adapters.driver.imp_drive_repo import ImpDriverRepo

from src.memoryEngine.internal.app.ports.memory.i_memory_task_producer import IMemoryTaskProducer
from src.memoryEngine.internal.infrastructure.adapters.memory.imp_memory_task_producer import ImpMemoryTaskProducer

from src.memoryEngine.internal.app.ports.memory.i_memory_repo import IMemoryRepo
from src.memoryEngine.internal.infrastructure.adapters.memory.imp_memory_repo import ImpMemoryRepo

from src.memoryEngine.internal.app.ports.network.i_network_task_producer import INetworkTaskProducer
from src.memoryEngine.internal.infrastructure.adapters.network.imp_network_task_producer import ImpNetworkTaskProducer

from src.memoryEngine.internal.app.ports.network.i_network_repo import INetworkRepo
from src.memoryEngine.internal.infrastructure.adapters.network.imp_network_repo import ImpNetworkRepo

from src.memoryEngine.internal.app.ports.console.i_console_task_producer import IConsoleTaskProducer
from src.memoryEngine.internal.infrastructure.adapters.console.imp_console_task_producer import ImpConsoleTaskProducer

from src.memoryEngine.internal.app.ports.console.i_console_repo import IConsoleRepo
from src.memoryEngine.internal.infrastructure.adapters.console.imp_console_repo import ImpConsoleRepo

from src.memoryEngine.internal.app.ports.i_project_repo import IProjectRepo
from src.memoryEngine.internal.infrastructure.adapters.imp_project_repo import ImpProjectRepo

from src.memoryEngine.internal.app.ports.handle.i_handle_task_producer import IHandleTaskProducer
from src.memoryEngine.internal.infrastructure.adapters.handle.imp_handle_task_producer import ImpHandleTaskProducer

from src.memoryEngine.internal.app.ports.handle.i_handle_repo import IHandleRepo
from src.memoryEngine.internal.infrastructure.adapters.handle.imp_handle_repo import ImpHandleRepo

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
from src.memoryEngine.internal.app.services.project_service import ProjectService
from src.memoryEngine.internal.app.services.handle.handle_task_service import HandleTaskService


# ====================== Services ==============================
def inject_process_task_producer() -> IProcessTaskProducer:
    return ImpProcessTaskProducer()

def inject_process_repo() -> IProcessRepo:
    return ImpProcessRepo()

def inject_process_task_service() -> ProcessTaskService:
    producer = inject_process_task_producer()
    return ProcessTaskService(producer)


# ====================== Registry ==============================
def inject_registry_task_producer() -> IRegistryTaskProducer:
    return ImpRegistryTaskProducer()

def inject_registry_repo() -> IRegistryRepo:
    return ImpRegistryRepo()

def inject_registry_task_service() -> RegistryTaskService:
    producer = inject_registry_task_producer()
    return RegistryTaskService(producer)


# ====================== Dll ==============================
def inject_dll_task_producer()-> IDllTaskProducer:
    return ImpDllTaskProducer()

def inject_dll_repo() -> IDllRepo:
    return ImpDllRepo()

def inject_dll_task_service() -> DllTaskService:
    producer = inject_dll_task_producer()
    return DllTaskService(producer)


# ====================== Activity ==============================
def inject_activity_task_producer() -> IActivityTaskProducer:
    return ImpActivityTaskProducer()

def inject_activity_repo() -> IActivityRepo:
    return ImpActivityRepo()

def inject_activity_task_service() -> ActivityTaskService:
    producer = inject_activity_task_producer()
    return ActivityTaskService(producer)


# ====================== Privilege ==============================
def inject_privilege_task_producer() -> IPrivilegeTaskProducer:
    return ImpPrivilegeTaskProducer()

def inject_privilege_repo() -> IPrivilegeRepo:
    return ImpPrivilegeRepo()

def inject_privilege_task_service() -> PrivilegeTaskService:
    producer = inject_privilege_task_producer()
    return PrivilegeTaskService(producer)

# ====================== File ==============================
def inject_file_task_producer() -> IFileTaskProducer:
    return ImpFileTaskProducer()

def inject_file_repo() -> IFileRepo:
    return ImpFileRepo()

def inject_file_task_service() -> FileTaskService:
    producer = inject_file_task_producer()
    return FileTaskService(producer)

# ====================== Service ==============================
def inject_service_task_producer() -> IServiceTaskProducer:
    return ImpServiceTaskProducer()

def inject_service_repo() -> IServiceRepo:
    return ImpServiceRepo()

def inject_service_task_service() -> ServiceTaskService:
    producer = inject_service_task_producer()
    return ServiceTaskService(producer)

# ====================== Driver ==============================
def inject_driver_task_producer() -> IDriverTaskProducer:
    return ImpDriverTaskProducer()

def inject_driver_repo() -> IDriverRepo:
    return ImpDriverRepo()

def inject_driver_task_service() -> DriverTaskService:
    producer = inject_driver_task_producer()
    return DriverTaskService(producer)

# ====================== Memory ==============================
def inject_memory_task_producer() -> IMemoryTaskProducer:
    return ImpMemoryTaskProducer()

def inject_memory_repo() -> IMemoryRepo:
    return ImpMemoryRepo()

def inject_memory_task_service() -> MemoryTaskService:
    producer = inject_memory_task_producer()
    return MemoryTaskService(producer)

# ====================== Network ==============================
def inject_network_task_producer() -> INetworkTaskProducer:
    return ImpNetworkTaskProducer()

def inject_network_repo() -> INetworkRepo:
    return ImpNetworkRepo()

def inject_network_task_service() -> NetworkTaskService:
    producer = inject_network_task_producer()
    return NetworkTaskService(producer)

# ====================== Console ==============================
def inject_console_task_producer() -> IConsoleTaskProducer:
    return ImpConsoleTaskProducer()

def inject_console_repo() -> IConsoleRepo:
    return ImpConsoleRepo()

def inject_console_task_service() -> ConsoleTaskService:
    producer = inject_console_task_producer()
    return ConsoleTaskService(producer)

# ====================== Project ==============================
def inject_project_repo() -> IProjectRepo:
    return ImpProjectRepo()

def inject_project_service() -> ProjectService:
    repo = inject_project_repo()
    return ProjectService(repo)

# ====================== Handle ==============================
def inject_handle_task_producer() -> IHandleTaskProducer:
    return ImpHandleTaskProducer()

def inject_handle_repo() -> IHandleRepo:
    return ImpHandleRepo()

def inject_handle_task_service() -> HandleTaskService:
    producer = inject_handle_task_producer()
    return HandleTaskService(producer)
from src.memoryHandling.app.ports.process.i_process_task_producer import IProcessTaskProducer
from src.memoryHandling.infrastructure.adapters.process.imp_process_task_producer import ImpProcessTaskProducer

from src.memoryHandling.app.ports.process.i_process_repo import IProcessRepo
from src.memoryHandling.infrastructure.adapters.process.imp_process_repo import ImpProcessRepo

from src.memoryHandling.app.ports.registry.i_registry_task_producer import IRegistryTaskProducer
from src.memoryHandling.infrastructure.adapters.registry.imp_registry_task_producer import ImpRegistryTaskProducer

from src.memoryHandling.app.ports.registry.i_registry_repo import IRegistryRepo
from src.memoryHandling.infrastructure.adapters.registry.imp_registry_repo import ImpRegistryRepo

from src.memoryHandling.app.ports.dll.i_dll_task_producer import IDllTaskProducer
from src.memoryHandling.infrastructure.adapters.dll.imp_dll_task_producer import ImpDllTaskProducer

from src.memoryHandling.app.ports.dll.i_dll_repo import IDllRepo
from src.memoryHandling.infrastructure.adapters.dll.imp_dll_repo import ImpDllRepo

from src.memoryHandling.app.services.process.process_task_service import ProcessTaskService
from src.memoryHandling.app.services.registry.process_task_service import RegistryTaskService
from src.memoryHandling.app.services.dll.dll_task_service import DllTaskService


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

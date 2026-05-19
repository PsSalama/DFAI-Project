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

from src.memoryHandling.app.ports.activity.i_activity_task_producer import IActivityTaskProducer
from src.memoryHandling.infrastructure.adapters.activity.imp_activity_task_producer import ImpActivityTaskProducer

from src.memoryHandling.app.ports.activity.i_activity_repo import IActivityRepo
from src.memoryHandling.infrastructure.adapters.activity.imp_activity_repo import ImpActivityRepo

from src.memoryHandling.app.ports.privilege.i_privilege_task_producer import IPrivilegeTaskProducer
from src.memoryHandling.infrastructure.adapters.privilege.imp_privilege_task_producer import ImpPrivilegeTaskProducer

from src.memoryHandling.app.ports.privilege.i_privilege_repo import IPrivilegeRepo
from src.memoryHandling.infrastructure.adapters.privilege.imp_privilege_repo import ImpPrivilegeRepo

from src.memoryHandling.app.services.process.process_task_service import ProcessTaskService
from src.memoryHandling.app.services.registry.process_task_service import RegistryTaskService
from src.memoryHandling.app.services.dll.dll_task_service import DllTaskService
from src.memoryHandling.app.services.activity.activity_task_service import ActivityTaskService
from src.memoryHandling.app.services.privilege.privilege_task_service import PrivilegeTaskService


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


# ====================== Dll ==============================
def inject_activity_task_producer() -> IActivityTaskProducer:
    return ImpActivityTaskProducer()

def inject_activity_repo() -> IActivityRepo:
    return ImpActivityRepo()

def inject_activity_task_service() -> ActivityTaskService:
    producer = inject_activity_task_producer()
    return ActivityTaskService(producer)


# ====================== Dll ==============================
def inject_privilege_task_producer() -> IPrivilegeTaskProducer:
    return ImpPrivilegeTaskProducer()

def inject_privilege_repo() -> IPrivilegeRepo:
    return ImpPrivilegeRepo()

def inject_privilege_task_service() -> PrivilegeTaskService:
    producer = inject_privilege_task_producer()
    return PrivilegeTaskService(producer)
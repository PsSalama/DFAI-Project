from src.memoryHandling.app.ports.process.i_process_task_producer import IProcessTaskProducer
from src.memoryHandling.infrastructure.adapters.process.imp_process_task_producer import ImpProcessTaskProducer

from src.memoryHandling.app.ports.process.i_process_repo import IProcessRepo
from src.memoryHandling.infrastructure.adapters.process.imp_process_repo import ImpProcessRepo

from src.memoryHandling.app.services.process.process_task_service import ProcessTaskService


def inject_process_task_producer() -> IProcessTaskProducer:
    return ImpProcessTaskProducer()


def inject_process_repo() -> IProcessRepo:
    return ImpProcessRepo()


def inject_process_task_service() -> ProcessTaskService:
    producer = inject_process_task_producer()
    return ProcessTaskService(producer)

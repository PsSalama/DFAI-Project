from src.memoryHandling.app.ports.process.i_task_producer import IProcessTaskProducer
from src.taskQueue.infrastructure.adapters.shared.memory.celery_process_task_producer import CeleryProcessTaskProducer

from src.memoryHandling.app.ports.process.i_process_repo import IProcessRepo
from src.memoryHandling.infrastructure.adapters.process.imp_process_repo import ImpProcessRepo

from src.memoryHandling.app.ports.process.i_data_parsing import IDataParsing
from src.memoryHandling.infrastructure.adapters.imp_data_parsing import ImpDataParsing

from src.memoryHandling.app.services.process.process_task_service import ProcessTaskService
from src.memoryHandling.app.services.process.process_handling_file_service import ProcessHandlingFileService


def inject_process_task_producer() -> IProcessTaskProducer:
    return CeleryProcessTaskProducer()


def inject_process_repo() -> IProcessRepo:
    return ImpProcessRepo()


def inject_data_parsing() -> IDataParsing:
    return ImpDataParsing()


def inject_process_task_service() -> ProcessTaskService:
    producer = inject_process_task_producer()
    return ProcessTaskService(producer)


def inject_process_handling_file_service() -> ProcessHandlingFileService:
    parsing = inject_data_parsing()
    repo = inject_process_repo()
    return ProcessHandlingFileService(
        parsing,
        repo
    )
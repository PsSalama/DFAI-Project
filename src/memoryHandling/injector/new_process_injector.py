from src.memoryHandling.app.ports.taskQueue.i_task_producer import IProcessTaskProducer
from src.taskQueue.infrastructure.adapters.shared.memory.celery_process_task_producer import CeleryProcessTaskProducer


def inject_process_task_producer() -> IProcessTaskProducer:
    return CeleryProcessTaskProducer()
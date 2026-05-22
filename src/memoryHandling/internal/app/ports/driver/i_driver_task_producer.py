from abc import ABC, abstractmethod
from src.memoryHandling.internal.app.dto.task_request import TaskRequest


class IDriverTaskProducer(ABC):
    @abstractmethod
    async def driver_scan_task(self, task_request: TaskRequest) -> dict:
        pass

    @abstractmethod
    async def driver_irp_task(self, task_request: TaskRequest) -> dict:
        pass
from abc import ABC, abstractmethod
from src.memoryHandling.internal.app.dto.task_request import TaskRequest


class IServiceTaskProducer(ABC):
    @abstractmethod
    async def service_scan_task(self, task_request: TaskRequest) -> dict:
        pass
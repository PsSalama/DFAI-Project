from abc import ABC, abstractmethod
from src.memoryHandling.internal.app.dto.task_request import TaskRequest


class IFileTaskProducer(ABC):
    @abstractmethod
    async def file_scan_task(self, task_request: TaskRequest) -> dict:
        pass

    @abstractmethod
    async def file_dump_task(self, task_request: TaskRequest) -> dict:
        pass

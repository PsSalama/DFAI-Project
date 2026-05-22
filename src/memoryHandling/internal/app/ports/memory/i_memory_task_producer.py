from abc import ABC, abstractmethod
from src.memoryHandling.internal.app.dto.task_request import TaskRequest


class IMemoryTaskProducer(ABC):
    @abstractmethod
    async def memory_info_task(self, task_request: TaskRequest) -> list[dict]:
        pass
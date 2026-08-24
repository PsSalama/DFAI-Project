from abc import ABC, abstractmethod
from src.memoryEngine.internal.app.dto.task_request import TaskRequest


class IKernalTaskProducer(ABC):
    @abstractmethod
    async def ssdt_task(self, task_request: TaskRequest) -> dict:
        pass
from abc import ABC, abstractmethod
from src.memoryEngine.internal.app.dto.task_request import TaskRequest


class IHandleTaskProducer(ABC):
    @abstractmethod
    async def handle_task(self, task_request: TaskRequest) -> dict:
        pass
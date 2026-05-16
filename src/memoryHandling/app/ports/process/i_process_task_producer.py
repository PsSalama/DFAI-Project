from abc import ABC, abstractmethod
from src.memoryHandling.app.dto.task_request import TaskRequest


class IProcessTaskProducer(ABC):
    @abstractmethod
    async def process_list_task(self, task_request: TaskRequest) -> dict:
        pass

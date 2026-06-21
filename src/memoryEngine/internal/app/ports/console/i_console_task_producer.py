from abc import ABC, abstractmethod
from src.memoryEngine.internal.app.dto.task_request import TaskRequest


class IConsoleTaskProducer(ABC):
    @abstractmethod
    async def console_task(self, task_request: TaskRequest) -> dict:
        pass


    @abstractmethod
    async def console_cmdscan_task(self, task_request: TaskRequest) -> dict:
        pass
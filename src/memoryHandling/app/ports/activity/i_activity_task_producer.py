from abc import ABC, abstractmethod
from src.memoryHandling.app.dto.task_request import TaskRequest


class IActivityTaskProducer(ABC):
    @abstractmethod
    async def activity_session_task(self, task_request: TaskRequest) -> dict:
        pass


    @abstractmethod
    async def activity_sid_task(self, task_request: TaskRequest) -> dict:
        pass


    @abstractmethod
    async def activity_desktop_task(self, task_request: TaskRequest) -> dict:
        pass

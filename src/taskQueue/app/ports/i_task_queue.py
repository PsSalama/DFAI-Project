from abc import ABC, abstractmethod
from src.taskQueue.app.dto.task_request import (TaskRequest)
from src.taskQueue.app.dto.task_response import (TaskResponse)


class ITaskQueue(ABC):
    @abstractmethod
    async def submit_task(self, task: TaskRequest) -> TaskResponse:
        pass

    @abstractmethod
    async def get_status(self, task_id: str) -> str:
        pass

    @abstractmethod
    async def get_result(self, task_id: str):
        pass
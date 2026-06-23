from abc import ABC, abstractmethod
from src.memoryEngine.internal.app.dto.task_request import TaskRequest


class IProcessTaskProducer(ABC):
    @abstractmethod
    async def process_view_task(self, task_request: TaskRequest) -> dict:
        pass

    @abstractmethod
    async def process_list_task(self, task_request: TaskRequest) -> dict:
        pass

    @abstractmethod
    async def process_scan_task(self, task_request: TaskRequest) -> dict:
        pass

    @abstractmethod
    async def process_tree_task(self, task_request: TaskRequest) -> dict:
        pass
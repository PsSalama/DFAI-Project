from abc import ABC, abstractmethod
from src.memoryEngine.internal.app.dto.task_request import TaskRequest


class INetworkTaskProducer(ABC):
    @abstractmethod
    async def network_scan_task(self, task_request: TaskRequest) -> dict:
        pass

    @abstractmethod
    async def network_stat_task(self, task_request: TaskRequest) -> dict:
        pass
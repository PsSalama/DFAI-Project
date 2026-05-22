from abc import ABC, abstractmethod
from src.memoryHandling.internal.app.dto.task_request import TaskRequest


class IRegistryTaskProducer(ABC):
    @abstractmethod
    async def registry_list_task(self, task_request: TaskRequest) -> dict:
        pass

    @abstractmethod
    async def registry_scan_task(self, task_request: TaskRequest) -> dict:
        pass

    @abstractmethod
    async def registry_key_task(self, task_request: TaskRequest) -> dict:
        pass

    @abstractmethod
    async def registry_cert_task(self, task_request: TaskRequest) -> dict:
        pass
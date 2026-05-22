from abc import ABC, abstractmethod
from src.memoryHandling.internal.app.dto.task_request import TaskRequest


class IDllTaskProducer(ABC):
    @abstractmethod
    async def dll_list_task(self, task_request: TaskRequest) -> dict:
        pass

    
    @abstractmethod
    async def dll_ldrmodules_task(self, task_request: TaskRequest) -> dict:
        pass


    @abstractmethod
    async def dll_module_task(self, task_request: TaskRequest) -> dict:
        pass


    @abstractmethod
    async def dll_modscan_task(self, task_request: TaskRequest) -> dict:
        pass
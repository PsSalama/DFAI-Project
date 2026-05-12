from abc import ABC, abstractmethod
from src.shared.dto.task_request import TaskRequest


class IProcessTaskProducer(ABC):
    @abstractmethod
    async def process_list_task(self, task_request: TaskRequest) -> dict:
        pass

    @abstractmethod
    async def process_tree_task(self, task_request: TaskRequest) -> dict:
        pass

    @abstractmethod
    async def process_hidden_task(self, task_request: TaskRequest) -> dict:
        pass

    @abstractmethod
    async def process_rootkit_task(self, task_request: TaskRequest) -> dict:
        pass

    @abstractmethod
    async def process_cmdline_task(self, task_request: TaskRequest) -> dict:
        pass

    @abstractmethod
    async def process_envars_task(self, task_request: TaskRequest) -> dict:
        pass

    @abstractmethod
    async def process_thrdscan_task(self, task_request: TaskRequest) -> dict:
        pass

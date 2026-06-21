from abc import ABC, abstractmethod
from src.memoryEngine.internal.app.dto.task_request import TaskRequest


class IPrivilegeTaskProducer(ABC):
    @abstractmethod
    async def privilege_process_task(self, task_request: TaskRequest) -> dict:
        pass

    @abstractmethod
    async def privilege_service_id_task(self, task_request: TaskRequest) -> dict:
        pass
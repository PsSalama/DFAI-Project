from abc import ABC, abstractmethod


class ITaskStatusReader(ABC):
    @abstractmethod
    async def get_task_status(self, task_id: str) -> dict:
        pass
from abc import ABC, abstractmethod


class IMemoryRepo(ABC):
    @abstractmethod
    def store_memory_info(self, memory_info: list[dict]):
        pass
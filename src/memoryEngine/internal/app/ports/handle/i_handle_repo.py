from abc import ABC, abstractmethod


class IHandleRepo(ABC):
    @abstractmethod
    def store_handle(self, file_scan: list[dict]):
        pass
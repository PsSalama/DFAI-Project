from abc import ABC, abstractmethod


class IKernalRepo(ABC):
    @abstractmethod
    def store_ssdt(self, file_scan: list[dict]):
        pass
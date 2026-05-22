from abc import ABC, abstractmethod


class IFileRepo(ABC):
    @abstractmethod
    def store_file_scan(self, file_scan: list[dict]):
        pass


    @abstractmethod
    def store_file_dump(self, file_dump: list[dict]):
        pass
from abc import ABC, abstractmethod


class IProcessRepo(ABC):
    @abstractmethod
    def store_process_view(self, process_view: list[dict]):
        pass


    @abstractmethod
    def store_process_list(self, process_list: list[dict]):
        pass


    @abstractmethod
    def store_process_scan(self, process_scan: list[dict]):
        pass


    @abstractmethod
    def store_process_tree(self, process_tree: list[dict]):
        pass
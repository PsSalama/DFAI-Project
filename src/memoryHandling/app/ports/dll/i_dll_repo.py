from abc import ABC, abstractmethod


class IDllRepo(ABC):
    @abstractmethod
    def store_dll_list(self, dll_list: list[dict]):
        pass


    @abstractmethod
    def store_dll_ldrmodule(self, process_list: list[dict]):
        pass


    @abstractmethod
    def store_dll_module(self, dll_list: list[dict]):
        pass


    @abstractmethod
    def store_dll_modscan(self, process_list: list[dict]):
        pass
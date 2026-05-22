from abc import ABC, abstractmethod


class IRegistryRepo(ABC):
    @abstractmethod
    def store_registry_list(self, registry_list: list[dict]):
        pass


    @abstractmethod
    def store_registry_scan(self, registry_scan: list[dict]):
        pass


    @abstractmethod
    def store_registry_key(self, registry_key: list[dict]):
        pass


    @abstractmethod
    def store_registry_cert(self, registry_cert: list[dict]):
        pass
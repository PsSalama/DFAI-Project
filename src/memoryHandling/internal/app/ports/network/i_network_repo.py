from abc import ABC, abstractmethod


class INetworkRepo(ABC):
    @abstractmethod
    def store_network_scan(self, network_scan: list[dict]):
        pass


    @abstractmethod
    def store_network_stat(self, network_stat: list[dict]):
        pass
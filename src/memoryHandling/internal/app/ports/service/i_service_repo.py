from abc import ABC, abstractmethod


class IServiceRepo(ABC):
    @abstractmethod
    def store_service_scan(self, service_scan: list[dict]):
        pass

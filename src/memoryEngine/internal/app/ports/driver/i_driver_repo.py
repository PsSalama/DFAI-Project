from abc import ABC, abstractmethod


class IDriverRepo(ABC):
    @abstractmethod
    def store_driver_scan(self, driver_scan: list[dict]):
        pass


    @abstractmethod
    def store_driver_irp(self, driver_irp: list[dict]):
        pass
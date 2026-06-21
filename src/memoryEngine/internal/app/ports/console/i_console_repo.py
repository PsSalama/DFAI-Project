from abc import ABC, abstractmethod


class IConsoleRepo(ABC):
    @abstractmethod
    def store_console(self, console: list[dict]):
        pass


    @abstractmethod
    def store_console_cmdscan(self, console_cmdscan: list[dict]):
        pass
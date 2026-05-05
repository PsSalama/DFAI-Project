from abc import ABC, abstractmethod
from src.memoryHandling.app.models.Process import Process

class IProcessRepo(ABC):
    @abstractmethod
    def process_list(self, ) -> list[Process]:
        pass

    @abstractmethod
    def process_tree(self, file_path:str ) -> list[Process]:
        pass

    @abstractmethod
    def process_hidden(self, file_path:str) -> list[Process]:
        pass

    @abstractmethod
    def process_command_line(self, file_path:str) -> list[Process]:
        pass

    @abstractmethod
    def process_environment_vars(self, file_path:str) -> list[Process]:
        pass

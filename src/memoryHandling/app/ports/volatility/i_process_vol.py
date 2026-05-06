from abc import ABC, abstractmethod

class IProcessVol(ABC):
    @abstractmethod
    def extract_process_list(self, file_path: str) -> list[dict]:
        pass

    @abstractmethod
    def extract_process_tree(self, file_path: str) -> list[dict]:
        pass

    @abstractmethod
    def extract_process_hidden(self, file_path: str) -> list[dict]:
        pass

    @abstractmethod
    def extract_process_command_line_args(self, file_path: str) -> list[dict]:
        pass

    @abstractmethod
    def extract_process_environment_vars(self, file_path: str) -> list[dict]:
        pass

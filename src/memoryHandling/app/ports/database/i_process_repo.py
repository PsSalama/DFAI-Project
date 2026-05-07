from abc import ABC, abstractmethod

class IProcessRepo(ABC):
    @abstractmethod
    def store_process_list(self,project_id: str, source_type: str, process_list: list[dict]):
        pass

    @abstractmethod
    def store_process_tree(self, project_id: str, source_type: str, process_tree: list[dict]):
        pass

    @abstractmethod
    def store_process_hidden(self, project_id: str, source_type: str, process_hidden: list[dict]):
        pass

    @abstractmethod
    def store_process_command_line(self, project_id: str, source_type: str, process_command_line: list[dict]):
        pass

    @abstractmethod
    def store_process_environment_vars(self, project_id: str, source_type: str, process_environment_vars: list[dict]):
        pass

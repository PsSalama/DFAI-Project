from abc import ABC, abstractmethod


class IProcessRepo(ABC):
    @abstractmethod
    def store_process_list(self, process_list: list[dict]):
        pass

    @abstractmethod
    def store_process_xview(self, process_list: list[dict]):
        pass

    @abstractmethod
    def store_process_tree(self, process_tree: list[dict]):
        pass

    @abstractmethod
    def store_process_hidden(self, process_hidden: list[dict]):
        pass

    @abstractmethod
    def store_process_command_line(self, process_command_line: list[dict]):
        pass

    @abstractmethod
    def store_process_environment_vars(self, process_environment_vars: list[dict]):
        pass

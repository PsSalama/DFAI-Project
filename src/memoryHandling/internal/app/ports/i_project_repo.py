from abc import ABC, abstractmethod


class IProjectRepo(ABC):
    @abstractmethod
    def delete_project(self):
        pass
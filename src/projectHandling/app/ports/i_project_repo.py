from abc import ABC, abstractmethod


class IProjectRepo(ABC):
    @abstractmethod
    def create_new_project(self, project_info: dict ) -> dict:
        pass

    @abstractmethod
    def get_project_by_id(self, project_id: str) -> dict:
        pass

    @abstractmethod
    def get_all_projects(self) -> list[dict]:
        pass
from src.projectHandling.app.ports.i_project_repo import IProjectRepo


class ProjectService:
    def __init__(self, i_project_repo: IProjectRepo):
        self.i_project_repo = i_project_repo


    def create_new_project(self, project_info: dict) -> dict:
        return self.i_project_repo.create_new_project(project_info)


    def get_project_by_id(self, project_id: str) -> dict:
        return self.i_project_repo.get_project_by_id(project_id)


    def get_all_projects(self) -> list[dict]:
        return self.i_project_repo.get_all_projects()
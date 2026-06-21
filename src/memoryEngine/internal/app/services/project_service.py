from src.memoryEngine.internal.app.ports.i_project_repo import IProjectRepo


class ProjectService:
    def __init__(self, repo: IProjectRepo):
        self.repo = repo

    def delete_project(self):
        self.repo.delete_project()
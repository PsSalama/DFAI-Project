from fastapi import Depends
from src.projectHandling.app.ports.i_project_repo import IProjectRepo
from src.projectHandling.app.services.project_service import ProjectService
from src.projectHandling.infrastructure.adapters.imp_project_repo import ImpProjectRepo


def inject_project_repo() -> IProjectRepo:
    return ImpProjectRepo()


def get_project_service(i_project_repo: IProjectRepo = Depends(inject_project_repo)) -> ProjectService:
    return ProjectService(
        i_project_repo
    )

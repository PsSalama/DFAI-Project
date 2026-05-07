from fastapi import APIRouter, Depends
from src.projectHandling.app.services.project_service import ProjectService
from src.projectHandling.app.dtos.project_info import CreateProjectInfo
from src.projectHandling.app.mapper.project_mapper import CreateProjectMapper
from src.projectHandling.injector.project_dependencies import get_project_service

router = APIRouter()

@router.post("/project")
def create_new_project(payload: CreateProjectInfo, project_service: ProjectService = Depends(get_project_service)) -> dict:
    create_project_mapper = CreateProjectMapper()
    payload_dict = create_project_mapper.from_dto_to_dict(payload)
    return project_service.create_new_project(payload_dict)
    

@router.get("/project/{project_id}")
def get_project_by_id(project_id: str, project_service: ProjectService = Depends(get_project_service)) -> dict:
    return project_service.get_project_by_id(project_id)


@router.get("/projects")
def get_all_projects(project_service: ProjectService = Depends(get_project_service)) -> list [dict]:
    return project_service.get_all_projects()
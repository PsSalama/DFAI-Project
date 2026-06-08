from fastapi import APIRouter, Depends, HTTPException
from src.memoryHandling.internal.app.services.project_service import ProjectService
from src.memoryHandling.internal.injector.injectors import inject_project_service


router = APIRouter()

@router.get("/project/delete")
async def project_clear(project_service: ProjectService = Depends(inject_project_service)):
    project_service.delete_project()
    return {"message": "Project has been deleted"}

from fastapi import APIRouter, Depends, HTTPException
from src.memoryEngine.internal.app.services.project_service import ProjectService
from src.memoryEngine.internal.injector.injectors import inject_project_service


router = APIRouter()

@router.get("/project/delete")
async def project_clear(project_service: ProjectService = Depends(inject_project_service)):
    project_service.delete_project()
    return {"message": "Project has been deleted"}

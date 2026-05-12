from src.taskQueue.app.services.task_status_service import TaskStatusService
from fastapi import APIRouter


router = APIRouter()


@router.get("/tasks/{task_id}")
async def get_task_status(task_id: str):
    return TaskStatusService.get_status(task_id)

from celery.result import AsyncResult
from src.taskQueue.infrastructure.config.celery_app import celery_app


class TaskStatusService:

    @staticmethod
    def get_status(task_id: str):

        result = AsyncResult(task_id, app=celery_app)

        return {
            "task_id": task_id,
            "status": result.status,
            "ready": result.ready(),
            "successful": result.successful(),
            "failed": result.failed(),
            "result": result.result if result.successful() else None
        }
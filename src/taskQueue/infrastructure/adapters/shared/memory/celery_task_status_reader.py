from celery.result import AsyncResult
from src.memoryHandling.app.ports.taskQueue.i_task_status_reader import ITaskStatusReader
from src.taskQueue.infrastructure.config.celery_app import celery_app


class CeleryTaskStatusReader(ITaskStatusReader):
    async def get_task_status(self, task_id: str) -> dict:
        result = AsyncResult(task_id, app=celery_app)
        return {
            "task_id": task_id,
            "status": result.status,
            "is_ready": result.ready(),
            "is_success": result.successful(),
            "is_failed": result.failed(),
            "result": result.result if result.successful() else None
        }
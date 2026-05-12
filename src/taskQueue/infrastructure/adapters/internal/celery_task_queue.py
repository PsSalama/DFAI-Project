from celery.result import AsyncResult
from src.taskQueue.app.ports.i_task_queue import (ITaskQueue)
from src.shared.dto.task_request import TaskRequest
from src.taskQueue.app.dto.task_response import (TaskResponse)
from infrastructure.config.celery_app import celery_app


class CeleryTaskQueue(ITaskQueue):
    async def submit_task(self, task: TaskRequest) -> TaskResponse:
        result = celery_app.send_task(
            task.task_name,
            kwargs=task.payload
        )
        return TaskResponse(
            task_id=result.id,
            status=result.status
        )


    async def get_status(self, task_id: str) -> str:
        result = AsyncResult(
            task_id,
            app=celery_app
        )
        return result.status


    async def get_result(self, task_id: str):
        result = AsyncResult(
            task_id,
            app=celery_app
        )
        return result.result
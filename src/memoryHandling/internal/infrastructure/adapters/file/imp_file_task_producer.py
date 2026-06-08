from src.memoryHandling.internal.app.ports.file.i_file_task_producer import IFileTaskProducer
from config.celery_app import celery_app
from config.redis_progress import redis_client
from src.memoryHandling.internal.app.dto.task_request import TaskRequest


class ImpFileTaskProducer(IFileTaskProducer):
    def __init__(self):
        redis_client.hincrby("workflow:progress", "all_tasks", 2)
        redis_client.hincrby("workflow:progress", "pending_tasks", 2)


    async def file_scan_task(self, task_request: TaskRequest) -> dict:
        # Send task to specific queue
        result = celery_app.send_task(
            task_request.task_name,
            kwargs=task_request.payload,
            queue="dfai_memory_qu",
            track_started=True,  # ✅ Track task progress
        )
        return {
            "task_id": result.id,
            "task_name": task_request.task_name,
            "status": "queued",
            "queue": "dfai_memory_qu"
        }


    async def file_dump_task(self, task_request: TaskRequest) -> dict:
        # Send task to specific queue
        result = celery_app.send_task(
            task_request.task_name,
            kwargs=task_request.payload,
            queue="dfai_memory_qu",
            track_started=True,  # ✅ Track task progress
        )
        return {
            "task_id": result.id,
            "task_name": task_request.task_name,
            "status": "queued",
            "queue": "dfai_memory_qu"
        }
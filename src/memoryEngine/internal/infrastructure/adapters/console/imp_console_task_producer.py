from src.memoryEngine.internal.app.ports.console.i_console_task_producer import IConsoleTaskProducer
from config.celery_app import celery_app
from config.redis_progress import redis_client
from src.memoryEngine.internal.app.dto.task_request import TaskRequest


class ImpConsoleTaskProducer(IConsoleTaskProducer):
    def __init__(self):
        redis_client.hincrby("workflow:progress", "all_tasks", 2)
        redis_client.hincrby("workflow:progress", "pending_tasks", 2)


    async def console_task(self, task_request: TaskRequest) -> dict:
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


    async def console_cmdscan_task(self, task_request: TaskRequest) -> dict:
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
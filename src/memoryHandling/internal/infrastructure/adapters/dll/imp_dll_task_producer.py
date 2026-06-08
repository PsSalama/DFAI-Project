from src.memoryHandling.internal.app.ports.dll.i_dll_task_producer import IDllTaskProducer
from config.celery_app import celery_app
from config.redis_progress import redis_client
from src.memoryHandling.internal.app.dto.task_request import TaskRequest


class ImpDllTaskProducer(IDllTaskProducer):
    def __init__(self):
        redis_client.hincrby("workflow:progress", "all_tasks", 4)
        redis_client.hincrby("workflow:progress", "pending_tasks", 4)


    async def dll_list_task(self, task_request: TaskRequest) -> dict:
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
        
    
    async def dll_ldrmodules_task(self, task_request: TaskRequest) -> dict:
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

    async def dll_module_task(self, task_request: TaskRequest) -> dict:
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

    async def dll_modscan_task(self, task_request: TaskRequest) -> dict:
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
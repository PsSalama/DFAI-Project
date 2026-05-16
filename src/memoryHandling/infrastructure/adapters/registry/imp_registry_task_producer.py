from src.memoryHandling.app.ports.registry.i_registry_task_producer import IRegistryTaskProducer
from config.celery_app import celery_app
from src.memoryHandling.app.dto.task_request import TaskRequest


class ImpRegistryTaskProducer(IRegistryTaskProducer):
    async def registry_list_task(self, task_request: TaskRequest) -> dict:
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


    async def registry_scan_task(self, task_request: TaskRequest) -> dict:
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


    async def registry_key_task(self, task_request: TaskRequest) -> dict:
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


    async def registry_cert_task(self, task_request: TaskRequest) -> dict:
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
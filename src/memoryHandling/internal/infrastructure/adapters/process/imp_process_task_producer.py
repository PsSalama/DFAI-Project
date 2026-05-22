from src.memoryHandling.internal.app.ports.process.i_process_task_producer import IProcessTaskProducer
from config.celery_app import celery_app
from src.memoryHandling.internal.app.dto.task_request import TaskRequest


class ImpProcessTaskProducer(IProcessTaskProducer):
    async def process_list_task(self, task_request: TaskRequest) -> dict:
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
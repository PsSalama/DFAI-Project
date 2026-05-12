from src.memoryHandling.app.ports.taskQueue.i_task_producer import IProcessTaskProducer
from src.taskQueue.infrastructure.config.celery_app import celery_app
from src.shared.dto.task_request import TaskRequest
import logging


logger = logging.getLogger(__name__)

class CeleryProcessTaskProducer(IProcessTaskProducer):
    async def process_list_task(self, task_request: TaskRequest) -> dict:
        logger.info(f"📤 Sending task: {task_request.task_name}")
        logger.info(f"   Payload: {task_request.payload}")
        # Send task to specific queue
        result = celery_app.send_task(
            task_request.task_name,
            kwargs=task_request.payload,
            queue="dfai_memory_qu",
            track_started=True,  # ✅ Track task progress
        )
        logger.info(f"✅ Task sent with ID: {result.id}")
        return {
            "task_id": result.id,
            "task_name": task_request.task_name,
            "status": "queued",
            "queue": "dfai_memory_qu"
        }


    async def process_tree_task(self, task_request: TaskRequest) -> dict:
        logger.info(f"📤 Sending task: {task_request.task_name}")
        logger.info(f"   Payload: {task_request.payload}")
        # Send task to specific queue
        result = celery_app.send_task(
            task_request.task_name,
            kwargs=task_request.payload,
            queue="dfai_memory_qu",
            track_started=True,  # ✅ Track task progress
        )
        logger.info(f"✅ Task sent with ID: {result.id}")
        return {
            "task_id": result.id,
            "task_name": task_request.task_name,
            "status": "queued",
            "queue": "dfai_memory_qu"
        }

    async def process_hidden_task(self, task_request: TaskRequest) -> dict:
        logger.info(f"📤 Sending task: {task_request.task_name}")
        logger.info(f"   Payload: {task_request.payload}")
        # Send task to specific queue
        result = celery_app.send_task(
            task_request.task_name,
            kwargs=task_request.payload,
            queue="dfai_memory_qu",
            track_started=True,  # ✅ Track task progress
        )
        logger.info(f"✅ Task sent with ID: {result.id}")
        return {
            "task_id": result.id,
            "task_name": task_request.task_name,
            "status": "queued",
            "queue": "dfai_memory_qu"
        }


    async def process_rootkit_task(self, task_request: TaskRequest) -> dict:
        logger.info(f"📤 Sending task: {task_request.task_name}")
        logger.info(f"   Payload: {task_request.payload}")
        # Send task to specific queue
        result = celery_app.send_task(
            task_request.task_name,
            kwargs=task_request.payload,
            queue="dfai_memory_qu",
            track_started=True,  # ✅ Track task progress
        )
        logger.info(f"✅ Task sent with ID: {result.id}")
        return {
            "task_id": result.id,
            "task_name": task_request.task_name,
            "status": "queued",
            "queue": "dfai_memory_qu"
        }

#######################################################
#######################################################

    async def process_cmdline_task(self, task_request: TaskRequest) -> dict:
        logger.info(f"📤 Sending task: {task_request.task_name}")
        logger.info(f"   Payload: {task_request.payload}")
        # Send task to specific queue
        result = celery_app.send_task(
            task_request.task_name,
            kwargs=task_request.payload,
            queue="dfai_memory_qu",
            track_started=True,  # ✅ Track task progress
        )
        logger.info(f"✅ Task sent with ID: {result.id}")
        return {
            "task_id": result.id,
            "task_name": task_request.task_name,
            "status": "queued",
            "queue": "dfai_memory_qu"
        }


    async def process_envars_task(self, task_request: TaskRequest) -> dict:
        logger.info(f"📤 Sending task: {task_request.task_name}")
        logger.info(f"   Payload: {task_request.payload}")
        # Send task to specific queue
        result = celery_app.send_task(
            task_request.task_name,
            kwargs=task_request.payload,
            queue="dfai_memory_qu",
            track_started=True,  # ✅ Track task progress
        )
        logger.info(f"✅ Task sent with ID: {result.id}")
        return {
            "task_id": result.id,
            "task_name": task_request.task_name,
            "status": "queued",
            "queue": "dfai_memory_qu"
        }


    async def process_thrdscan_task(self, task_request: TaskRequest) -> dict:
        logger.info(f"📤 Sending task: {task_request.task_name}")
        logger.info(f"   Payload: {task_request.payload}")
        # Send task to specific queue
        result = celery_app.send_task(
            task_request.task_name,
            kwargs=task_request.payload,
            queue="dfai_memory_qu",
            track_started=True,  # ✅ Track task progress
        )
        logger.info(f"✅ Task sent with ID: {result.id}")
        return {
            "task_id": result.id,
            "task_name": task_request.task_name,
            "status": "queued",
            "queue": "dfai_memory_qu"
        }
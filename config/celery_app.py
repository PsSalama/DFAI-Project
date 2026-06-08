import os
from celery import Celery
from dotenv import load_dotenv
from celery.signals import worker_process_init
from config.database import Database
import config.celery_signals


load_dotenv()

celery_app = Celery(
    "dfai_celery",
    broker=os.environ.get("CELERY_BROKER_URL"),
    backend=os.environ.get("CELERY_RESULT_BACKEND"),
    include=[
        "src.memoryHandling.internal.infrastructure.consumer.process_tasks",
        "src.memoryHandling.internal.infrastructure.consumer.registry_tasks",
        "src.memoryHandling.internal.infrastructure.consumer.dll_tasks",
        "src.memoryHandling.internal.infrastructure.consumer.activity_tasks",
        "src.memoryHandling.internal.infrastructure.consumer.privilege_tasks",
        "src.memoryHandling.internal.infrastructure.consumer.file_tasks",
        "src.memoryHandling.internal.infrastructure.consumer.service_tasks",
        "src.memoryHandling.internal.infrastructure.consumer.driver_tasks",
        "src.memoryHandling.internal.infrastructure.consumer.memory_tasks",
        "src.memoryHandling.internal.infrastructure.consumer.network_tasks",
        "src.memoryHandling.internal.infrastructure.consumer.console_tasks"
    ]
)

# for initialize database connection inside celery worker.
@worker_process_init.connect
def init_worker(**kwargs):
    Database.init_db()


celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    task_time_limit=os.environ.get("CELERY_TASK_TIME_LIMIT", 300),
    task_soft_time_limit=os.environ.get("CELERY_TASK_Soft_TIME_LIMIT", 240),
    task_acks_late=os.environ.get("CELERY_ACKS_LATE"),
    worker_prefetch_multiplier=1,
)


# __all__ = ["celery_app"]
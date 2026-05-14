import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

celery_app = Celery(
    "dfai_celery",
    broker=os.environ.get("CELERY_BROKER_URL"),
    backend=os.environ.get("CELERY_RESULT_BACKEND"),
    include=[
        "src.memoryHandling.infrastructure.consumer.process.process_tasks",
        "src.memoryHandling.infrastructure.consumer.process.file_parsing"
    ]
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    task_time_limit=os.environ.get("CELERY_TASK_TIME_LIMIT"),
    task_soft_time_limit=os.environ.get("CELERY_TASK_Soft_TIME_LIMIT"),
    task_acks_late=os.environ.get("CELERY_ACKS_LATE"),
    worker_prefetch_multiplier=1,
)


# __all__ = ["celery_app"]
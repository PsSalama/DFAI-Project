from celery import Celery
from config.config import settings


celery_app = Celery(
    "dfai_celery",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    task_time_limit=settings.CELERY_TASK_TIME_LIMIT,
    task_soft_time_limit=settings.CELERY_TASK_SOFT_TIME_LIMIT,
    task_default_queue=settings.CELERY_QUEUE_NAME,
    task_acks_late=settings.CELERY_ACKS_LATE,
    worker_prefetch_multiplier=1,
)

celery_app.autodiscover_tasks([
    "src.taskQueue.infrastructure.tasks"
])

__all__ = ["celery_app"]
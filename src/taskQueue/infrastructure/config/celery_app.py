from celery import Celery
import os
from pathlib import Path
import sys

# Add project root to path
project_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(project_root))


# Import settings
try:
    from config.config import settings
    BROKER_URL = settings.CELERY_BROKER_URL
    BACKEND_URL = settings.CELERY_RESULT_BACKEND
    QUEUE_NAME = settings.CELERY_QUEUE_NAME
except ImportError:
    # Fallback to environment variables
    BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
    BACKEND_URL = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/1")
    QUEUE_NAME = os.getenv("CELERY_QUEUE_NAME", "dfai_memory_qu")

# Create Celery app
celery_app = Celery(
    "dfai_celery",
    broker=BROKER_URL,
    backend=BACKEND_URL,
)

# Configure Celery
celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    task_track_started=True,
    task_time_limit=7200,
    task_default_queue=QUEUE_NAME,
    task_acks_late=True,
    worker_prefetch_multiplier=1,
)

# Auto-discover tasks
celery_app.autodiscover_tasks([
    'src.taskQueue.infrastructure.tasks',
])

__all__ = ['celery_app']
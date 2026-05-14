# taskQueue/infrastructure/workers/celery_worker.py
import sys
from pathlib import Path


project_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(project_root))


# Import Celery app
from src.taskQueue.infrastructure.config.celery_app import celery_app

# Import tasks to register them

if __name__ == "__main__":
    celery_app.worker_main([
        'worker',
        '--loglevel=info',
        '--queues=dfai_memory_qu',  # we can add many of queues and celery can work on all of then in the same time
        '--concurrency=1',
        '--pool=solo',  # ✅ Fixes Windows permission errors
        '--without-gossip',
        '--without-mingle',
        '--without-heartbeat',
    ])


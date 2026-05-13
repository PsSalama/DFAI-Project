# taskQueue/infrastructure/workers/celery_worker.py
import sys
from pathlib import Path


project_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(project_root))

print(f"✅ Project root: {project_root}")

# Import Celery app
from infrastructure.config.celery_app import celery_app

# Import tasks to register them

if __name__ == "__main__":
    print("\n🚀 Starting Celery Worker...")
    print(f"   Queue: dfai_memory_qu")
    print("-" * 50)

    celery_app.worker_main([
        'worker',
        '--loglevel=info',
        '--queues=dfai_memory_qu',
        '--concurrency=1',
        '--pool=solo',  # ✅ Fixes Windows permission errors
        '--without-gossip',
        '--without-mingle',
        '--without-heartbeat',
    ])


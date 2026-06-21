from celery.signals import task_postrun
from config.redis_progress import redis_client
from src.memoryEngine.internal.infrastructure.pubSub.publisher import Publisher


@task_postrun.connect
def update_workflow_progress(sender=None, state=None, **kwargs):
    if state != "SUCCESS":
        return

    key = "workflow:progress"
    redis_client.hincrby(key, "finished_tasks", 1) # Update finished_tasks counter
    redis_client.hincrby(key, "pending_tasks", -1) # Update pending_tasks counter

    # Read current progress
    progress = redis_client.hgetall(key)
    all_tasks = int(progress.get("all_tasks", 0))
    finished_tasks = int(progress.get("finished_tasks", 0))
    pending_tasks = int(progress.get("pending_tasks", 0))

    # Calculate percentage
    percentage = (
        round((finished_tasks / all_tasks) * 100, 2)
        if all_tasks > 0
        else 0
    )
    redis_client.hset(key, "percentage", percentage) # Update percentage counter

    publisher = Publisher()
    publisher.publish_progress({
        "event": "progress_updated",
        "all_tasks": all_tasks,
        "finished_tasks": finished_tasks,
        "pending_tasks": pending_tasks,
        "percentage": percentage
    })
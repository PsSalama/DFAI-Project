from src.taskQueue.infrastructure.config.celery_app import celery_app
from src.taskQueue.infrastructure.executors.volatility_executor import run_volatility
from src.taskQueue.infrastructure.publishers.event_bus import EventBus


event_bus = EventBus()

@celery_app.task(bind=True, name="process_list_task")
def process_list_task(self, file_path: str, plugin: str):
    try:
        output_file = f"{plugin.replace('.', '_')}.txt"
        result = run_volatility(file_path, plugin, output_file)
        event_bus.publish(
            "task_process_events",
            {
                "event": "PROCESS_COMPLETED",
                "task_id": self.request.id,
                "plugin": plugin,
                "file_path": file_path,
                "output_file": output_file
            }
        )
        return {
            "status": "success",
            "task_id": self.request.id,
            "result": result
        }
    except Exception as e:
        raise
from config.celery_app import celery_app
from src.memoryHandling.internal.infrastructure.adapters.activity.imp_activity_repo import ImpActivityRepo
from src.memoryHandling.internal.infrastructure.services.volatility_tool import run_volatility
from src.memoryHandling.internal.app.services.activity.activity_store_service import ActivityStoreService


repo = ImpActivityRepo()
activity_store_service = ActivityStoreService(repo)

@celery_app.task(bind=True, name="activity_session_task")
def activity_session_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    activity_store_service.store_activity_session(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }


@celery_app.task(bind=True, name="activity_sid_task")
def activity_sid_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    activity_store_service.store_activity_sid(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }


@celery_app.task(bind=True, name="activity_desktop_task")
def activity_desktop_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    activity_store_service.store_activity_desktop(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }
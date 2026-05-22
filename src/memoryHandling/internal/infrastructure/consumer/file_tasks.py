from config.celery_app import celery_app
from src.memoryHandling.internal.infrastructure.adapters.file.imp_file_repo import ImpFileRepo
from src.memoryHandling.internal.infrastructure.services.volatility_tool import run_volatility
from src.memoryHandling.internal.app.services.file.file_store_service import FileStoreService


repo = ImpFileRepo()
file_store_service = FileStoreService(repo)

@celery_app.task(bind=True, name="file_scan_task")
def file_scan_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    file_store_service.store_file_scan(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }


@celery_app.task(bind=True, name="file_dump_task")
def file_dump_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    file_store_service.store_file_dump(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }
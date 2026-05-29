from config.celery_app import celery_app
from src.memoryHandling.internal.infrastructure.adapters.console.imp_console_repo import ImpConsoleRepo
from src.memoryHandling.internal.infrastructure.services.volatility_tool import run_volatility
from src.memoryHandling.internal.app.services.console.console_store_service import ConsoleStoreService


repo = ImpConsoleRepo()
console_store_service = ConsoleStoreService(repo)

@celery_app.task(bind=True, name="console_task")
def console_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    console_store_service.store_console(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }


@celery_app.task(bind=True, name="console_cmdscan_task")
def console_cmdscan_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    console_store_service.store_console_cmdscan(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }
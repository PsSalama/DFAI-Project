from config.celery_app import celery_app
from src.memoryEngine.internal.infrastructure.adapters.handle.imp_handle_repo import ImpHandleRepo
from src.memoryEngine.internal.infrastructure.services.volatility_tool import run_volatility
from src.memoryEngine.internal.app.services.handle.handle_store_service import HandleStoreService


repo = ImpHandleRepo()
handle_store_service = HandleStoreService(repo)

@celery_app.task(bind=True, name="handle_task")
def handle_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    handle_store_service.store_handle(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }
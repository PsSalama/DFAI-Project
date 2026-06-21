from config.celery_app import celery_app
from src.memoryEngine.internal.infrastructure.services.volatility_tool import run_volatility
from src.memoryEngine.internal.app.services.process.process_store_service import ProcessStoreService
from src.memoryEngine.internal.infrastructure.adapters.process.imp_process_repo import ImpProcessRepo


repo = ImpProcessRepo()
process_store_service = ProcessStoreService(repo)

@celery_app.task(bind=True, name="process_list_task")
def process_list_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    process_store_service.store(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }
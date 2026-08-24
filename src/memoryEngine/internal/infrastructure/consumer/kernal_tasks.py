from config.celery_app import celery_app
from src.memoryEngine.internal.infrastructure.adapters.kernal.imp_kernal_repo import ImpKernalRepo
from src.memoryEngine.internal.infrastructure.services.volatility_tool import run_volatility
from src.memoryEngine.internal.app.services.kernal.kernal_store_service import KernalStoreService


repo = ImpKernalRepo()
kernal_store_service = KernalStoreService(repo)

@celery_app.task(bind=True, name="ssdt_task")
def ssdt_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    kernal_store_service.store_ssdt(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }
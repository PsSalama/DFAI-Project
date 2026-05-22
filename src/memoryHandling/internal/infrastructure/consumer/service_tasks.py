from config.celery_app import celery_app
from src.memoryHandling.internal.infrastructure.services.volatility_tool import run_volatility
from src.memoryHandling.internal.app.services.service.service_store_service import ServiceStoreService
from src.memoryHandling.internal.infrastructure.adapters.service.imp_service_repo import ImpServiceRepo


repo = ImpServiceRepo()
service_store_service = ServiceStoreService(repo)

@celery_app.task(bind=True, name="service_scan_task")
def service_scan_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    service_store_service.store_service_scan(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }
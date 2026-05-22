from config.celery_app import celery_app
from src.memoryHandling.internal.infrastructure.services.volatility_tool import run_volatility
from src.memoryHandling.internal.app.services.driver.driver_store_service import DriverStoreService
from src.memoryHandling.internal.infrastructure.adapters.driver.imp_drive_repo import ImpDriverRepo


repo = ImpDriverRepo()
driver_store_service = DriverStoreService(repo)

@celery_app.task(bind=True, name="driver_scan_task")
def driver_scan_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    driver_store_service.store_driver_scan(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }


@celery_app.task(bind=True, name="driver_irp_task")
def driver_irp_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    driver_store_service.store_driver_irp(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }
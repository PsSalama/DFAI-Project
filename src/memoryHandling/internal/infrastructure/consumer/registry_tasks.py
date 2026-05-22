from config.celery_app import celery_app
from src.memoryHandling.internal.infrastructure.services.volatility_tool import run_volatility
from src.memoryHandling.internal.app.services.registry.registry_store_service import RegistryStoreService
from src.memoryHandling.internal.infrastructure.adapters.registry.imp_registry_repo import ImpRegistryRepo


repo = ImpRegistryRepo()
registry_store_service = RegistryStoreService(repo)

@celery_app.task(bind=True, name="registry_list_task")
def registry_list_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    registry_store_service.store_registry_list(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }


@celery_app.task(bind=True, name="registry_scan_task")
def registry_scan_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    registry_store_service.store_registry_scan(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }


@celery_app.task(bind=True, name="registry_key_task")
def registry_key_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    registry_store_service.store_registry_key(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }


@celery_app.task(bind=True, name="registry_cert_task")
def registry_cert_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    registry_store_service.store_registry_cert(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }
from config.celery_app import celery_app
from src.memoryEngine.internal.infrastructure.services.volatility_tool import run_volatility
from src.memoryEngine.internal.app.services.dll.dll_store_service import DllStoreService
from src.memoryEngine.internal.infrastructure.adapters.dll.imp_dll_repo import ImpDllRepo


repo = ImpDllRepo()
dll_store_service = DllStoreService(repo)

@celery_app.task(bind=True, name="dll_list_task")
def dll_list_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    dll_store_service.store_dll_list(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }


@celery_app.task(bind=True, name="dll_ldrmodules_task")
def dll_ldrmodules_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    dll_store_service.store_dll_ldrmodules(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }

@celery_app.task(bind=True, name="dll_module_task")
def dll_module_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    dll_store_service.store_dll_list(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }


@celery_app.task(bind=True, name="dll_modscan_task")
def dll_modscan_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    dll_store_service.store_dll_ldrmodules(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }
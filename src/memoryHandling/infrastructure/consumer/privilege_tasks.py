from config.celery_app import celery_app
from src.memoryHandling.infrastructure.adapters.privilege.imp_privilege_repo import ImpPrivilegeRepo
from src.memoryHandling.infrastructure.tools.volatility_tool import run_volatility
from src.memoryHandling.app.services.privilege.privilege_store_service import PrivilegeStoreService


repo = ImpPrivilegeRepo()
privilege_store_service = PrivilegeStoreService(repo)

@celery_app.task(bind=True, name="privilege_process_task")
def privilege_process_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    privilege_store_service.store_privilege_process(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }


@celery_app.task(bind=True, name="privilege_service_id_task")
def privilege_service_id_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    privilege_store_service.store_privilege_service_id(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }
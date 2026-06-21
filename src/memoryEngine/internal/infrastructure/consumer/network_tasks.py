from config.celery_app import celery_app
from src.memoryEngine.internal.infrastructure.services.volatility_tool import run_volatility
from src.memoryEngine.internal.app.services.network.network_store_service import NetworkStoreService
from src.memoryEngine.internal.infrastructure.adapters.network.imp_network_repo import ImpNetworkRepo


repo = ImpNetworkRepo()
network_store_service = NetworkStoreService(repo)

@celery_app.task(bind=True, name="network_scan_task")
def network_scan_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    network_store_service.store_network_scan(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }


@celery_app.task(bind=True, name="network_stat_task")
def network_stat_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    network_store_service.store_network_stat(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }
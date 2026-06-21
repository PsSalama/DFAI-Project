from config.celery_app import celery_app
from src.memoryEngine.internal.infrastructure.adapters.memory.imp_memory_repo import ImpMemoryRepo
from src.memoryEngine.internal.infrastructure.services.volatility_tool_one import run_volatility
from src.memoryEngine.internal.app.services.memory.memory_store_service import MemoryStoreService


repo = ImpMemoryRepo()
memory_store_service = MemoryStoreService(repo)

@celery_app.task(bind=True, name="memory_info_task")
def memory_info_task(self, file_path: str, plugin: str):
    result = run_volatility(file_path, plugin)
    memory_store_service.store_memory_info(result)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "parsed_data": result
    }
from config.celery_app import celery_app
from src.memoryHandling.infrastructure.tools.volatility_tool import run_volatility
from src.memoryHandling.infrastructure.parser.file_parsing import parse_artifacts_task
from src.memoryHandling.app.services.process.process_store_service import ProcessStoreService
from src.memoryHandling.infrastructure.adapters.process.imp_process_repo import ImpProcessRepo


repo = ImpProcessRepo()
process_store_service = ProcessStoreService(repo)

@celery_app.task(bind=True, name="process_list_task")
def process_list_task(self, file_path: str, plugin: str):
    output_file = f"{plugin.replace('.', '_')}.txt"
    result = run_volatility(file_path, plugin, output_file)
    parsed_data = parse_artifacts_task(output_file)
    process_store_service.store(parsed_data)
    return {
        "status": "success",
        "task_id": self.request.id,
        "result": result,
        "plugin": plugin,
        "output_file": output_file,
        "parsed_data": parsed_data
    }
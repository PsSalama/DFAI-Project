import asyncio
from src.memoryHandling.app.services.process.process_list_service import ProcessListService
from src.memoryHandling.app.services.process.process_tree_service import ProcessTreeService
from src.memoryHandling.app.services.process.process_hidden_service import ProcessHiddenService
from src.memoryHandling.app.services.process.process_command_line_service import ProcessCommandLineService
from src.memoryHandling.app.services.process.process_environment_vars_service import ProcessEnvironmentVarsService


class ProcessMainService:
    def __init__(
        self,
        process_list_service: ProcessListService,
        process_tree_service: ProcessTreeService,
        process_hidden_service: ProcessHiddenService,
        process_command_line_service: ProcessCommandLineService,
        process_environment_vars_service: ProcessEnvironmentVarsService
    ):
        self.process_list_service = process_list_service
        self.process_tree_service = process_tree_service
        self.process_hidden_service = process_hidden_service
        self.process_command_line_service = process_command_line_service
        self.process_environment_vars_service = process_environment_vars_service


    async def process_main_service(self, project_id: str, source_type: str, memory_file_path: str):
        await self.process_service(project_id, source_type, memory_file_path)


    async def process_service(self, project_id: str, source_type: str, memory_file_path: str):
        await asyncio.gather(
            asyncio.to_thread(self.process_list_service.process_handling, project_id, source_type, memory_file_path),
            asyncio.to_thread(self.process_tree_service.process_handling,project_id, source_type, memory_file_path),
            asyncio.to_thread(self.process_hidden_service.process_handling,project_id, source_type, memory_file_path),
            asyncio.to_thread(self.process_command_line_service.process_handling,project_id, source_type, memory_file_path),
            asyncio.to_thread(self.process_environment_vars_service.process_handling,project_id, source_type, memory_file_path)
        )


class MainService:
    def __init__(self, process_main_service):
        self.process_main_service = process_main_service


    async def main(self, project_id, source_type, memory_file_path):
        await self.process_main_service.process_main_service(project_id, source_type, memory_file_path)
        return {
            "message": "Analysis completed"
        }
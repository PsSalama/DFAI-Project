from src.memoryHandling.app.ports.database.i_process_repo import IProcessRepo
from src.memoryHandling.app.ports.volatility.i_process_vol import IProcessVol


class ProcessListService:
    def __init__(
            self,
            i_process_vol:IProcessVol,
            i_process_repo:IProcessRepo
    ):
        self.i_process_vol = i_process_vol
        self.i_process_repo = i_process_repo


    def process_handling(self, project_id: str, source_type: str, file_path: str):
        extracted_processes = self.extract_process_from_volatility(file_path)
        return self.store_process_in_database(project_id, source_type, extracted_processes)


    def extract_process_from_volatility(self, file_path: str) -> list[dict]:
        return self.i_process_vol.extract_process_list(file_path)


    def store_process_in_database(self, project_id, source_type: str, processes_lists: list[dict]) -> list[dict]:
        return self.i_process_repo.store_process_list(project_id, source_type, processes_lists)

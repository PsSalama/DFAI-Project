from src.memoryHandling.app.ports.database.i_process_repo import IProcessRepo
from src.memoryHandling.app.ports.volatility.i_process_vol import IProcessVol

class ProcessListService:
    def __init__(self, i_process_vol:IProcessVol, i_process_repo:IProcessRepo):
        self.i_process_vol = i_process_vol
        self.i_process_repo = i_process_repo


    def process_handling(self, file_path: str):
        extracted_processes = self.extract_process_from_volatility(file_path)
        stored_processes = self.store_process_in_database(extracted_processes)


    def extract_process_from_volatility(self, file_path: str) -> list[dict]:
        raw_processes = self.i_process_vol.extract_process_list(file_path)
        return raw_processes


    def store_process_in_database(self, processes_lists: list[dict]) -> list[dict]:
        return self.i_process_repo.store_process_list(processes_lists) # To sent data extracted from volatility to repo interface


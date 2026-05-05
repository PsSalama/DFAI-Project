from src.memoryHandling.app.ports.volatility.IProcesses import IProcesses
from src.memoryHandling.app.models.Process import *

class ProcessListService:
    def __init__(self, iprocess: IProcesses):
        self.iprocess = iprocess

    def process_list(self, file_path:str) -> list[ProcessList]:
        return self.iprocess.process_list(file_path)

from src.memoryHandling.app.ports.volatility.i_process_vol import IProcesses
from src.memoryHandling.app.models.process import *

# Dependency Injection through constructor
class ProcessTreeService:
    def __init__(self, processes_impl: IProcesses):
        self.processes_impl = processes_impl

    def process_list(self, file_path: str) -> list[ProcessTree]:
        return self.processes_impl.process_tree(file_path)

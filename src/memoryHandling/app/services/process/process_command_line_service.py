from src.memoryHandling.app.ports.volatility.i_process_vol import IProcesses
from src.memoryHandling.app.models.process import *

# Dependency Injection through constructor
class ProcessCommandLineService:
    def __init__(self, processes_impl: IProcesses):
        self.processes_impl = processes_impl

    def process_command_line(self, file_path: str) -> list[ProcessCommandLine]:
        return self.processes_impl.process_command_line_args(file_path)

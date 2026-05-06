from src.memoryHandling.app.ports.volatility.i_process_vol import IProcesses
from src.memoryHandling.app.models.process import *

# Dependency Injection through constructor
class ProcessEnvironmentVarsService:
    def __init__(self, processes_impl: IProcesses):
        self.processes_impl = processes_impl

    def process_environment_vars(self, file_path: str) -> list[ProcessEnvironmentVars]:
        return self.processes_impl.process_environment_vars(file_path)

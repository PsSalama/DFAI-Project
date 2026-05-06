import subprocess
from typing import List

from src.memoryHandling.infrastructure.mappers.process_mapper_dict_database import ProcessListMapperToDatabaseModel
from src.memoryHandling.app.ports.volatility.i_process_vol import IProcessVol
from src.memoryHandling.infrastructure.parser.process_parser import *
from src.memoryHandling.infrastructure.models.process.process_list_model import ProcessListModel
from src.memoryHandling.infrastructure.models.process.process_tree_model import ProcessTreeModel
from src.memoryHandling.infrastructure.models.process.process_hidden_model import ProcessHiddenModel
from src.memoryHandling.infrastructure.models.process.process_command_line_model import ProcessCommandLineModel
from src.memoryHandling.infrastructure.models.process.process_environment_vars_model import ProcessEnvironmentVarsModel
from src.memoryHandling.infrastructure.mappers.process_mapper_vol_dict import *

class ImpProcesses(IProcessVol):
    def __init__(self):
        self.parser = ProcessListParser()


    def run_volatility(self, file_path: str, plugin: str, file_name: str) -> str:
        result = subprocess.run(
            ["vol", "-f", file_path, plugin],
            capture_output=True,
            text=True
        )
        output_path = "resources/" + file_name
        with open("resources/"+file_name, "w", encoding="utf-8") as f:
            f.write(result.stdout)
        return output_path


    def extract_process_list(self, file_path: str) -> List[dict]:
        output_file = self.run_volatility(
            file_path,
            "windows.pslist",
            "process_list.txt"
        )
        parsed = self.parser.parse_pslist(output_file)
        #print(parsed)
        return parsed


    def extract_process_tree(self, file_path: str) -> List[dict]:
        raw = self.run_volatility(file_path, "windows.pstree")
        parsed = self.parse_rows(raw)
        return [ProcessTreeModel(**e) for e in parsed]


    def extract_process_hidden(self, file_path: str) -> List[ProcessHiddenModel]:
        raw = self.run_volatility(file_path, "windows.psxview")
        parsed = self.parse_rows(raw)
        return [ProcessHiddenModel(**e) for e in parsed]


    def extract_process_command_line_args(self, file_path: str) -> List[ProcessCommandLineModel]:
        raw = self.run_volatility(file_path, "windows.cmdline")
        parsed = self.parse_rows(raw)
        return [ProcessCommandLineModel(**e) for e in parsed]


    def extract_process_environment_vars(self, file_path: str) -> List[ProcessEnvironmentVarsModel]:
        raw = self.run_volatility(file_path, "windows.envars")
        parsed = self.parse_rows(raw)
        return [ProcessEnvironmentVarsModel(**e) for e in parsed]

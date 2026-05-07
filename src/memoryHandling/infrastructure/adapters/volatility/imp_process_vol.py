import subprocess
import os
from src.memoryHandling.app.ports.volatility.i_process_vol import IProcessVol
from src.memoryHandling.infrastructure.parser.process_parser import ProcessParser
from src.memoryHandling.infrastructure.mappers.process_mapper_vol_dict import *


class ImpProcesses(IProcessVol):
    @staticmethod
    def run_volatility(file_path: str, plugin: str, file_name: str) -> str:
        result = subprocess.run(
            ["vol", "-f", file_path, plugin],
            capture_output=True,
            text=True
        )
        output_dir = "resources"
        # Create folder if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, file_name)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(result.stdout)
        return output_path


    def extract_process_list(self, file_path: str) -> list[dict]:
        output_file = ImpProcesses.run_volatility(
            file_path,
            "windows.pslist",
            "process_list.txt"
        )
        data_parsed = ProcessParser.process_parse(output_file)
        data_mapped = [
            ProcessListMapperToDict.vol_to_dict(process)
            for process in data_parsed
        ]
        return data_mapped


    def extract_process_tree(self, file_path: str) -> list[dict]:
        output_file = self.run_volatility(
            file_path,
            "windows.pstree",
            "process_tree.txt"
        )
        data_parsed = ProcessParser.process_parse(output_file)
        data_mapped = [
            ProcessTreeMapperToDict.vol_to_dict(process)
            for process in data_parsed
        ]
        return data_mapped


    def extract_process_hidden(self, file_path: str) -> list[dict]:
        output_file = self.run_volatility(
            file_path,
            "windows.psxview",
            "process_psxview.txt"
        )
        data_parsed = ProcessParser.process_parse(output_file)
        data_mapped = [
            ProcessHiddenMapperToDict.vol_to_dict(process)
            for process in data_parsed
        ]
        return data_mapped


    def extract_process_command_line_args(self, file_path: str) -> list[dict]:
        output_file = self.run_volatility(
            file_path,
            "windows.cmdline",
            "process_cmdline.txt"
        )
        data_parsed = ProcessParser.process_parse(output_file)
        data_mapped = [
            ProcessCommandLineMapperToDict.vol_to_dict(process)
            for process in data_parsed
        ]
        return data_mapped


    def extract_process_environment_vars(self, file_path: str) -> list[dict]:
        output_file = self.run_volatility(
            file_path,
            "windows.envars",
            "process_envars.txt"
        )
        data_parsed = ProcessParser.process_parse(output_file)
        data_mapped = [
            ProcessListMapperToDict.vol_to_dict(process)
            for process in data_parsed
        ]
        return data_mapped
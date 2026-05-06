import subprocess
from src.memoryHandling.app.ports.volatility.i_process_vol import IProcessVol
from src.memoryHandling.infrastructure.parser.process_parser import *


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


    def extract_process_list(self, file_path: str) -> list[dict]:
        output_file = self.run_volatility(
            file_path,
            "windows.pslist",
            "process_list.txt"
        )
        parsed = self.parser.parse_pslist(output_file)
        return parsed


    def extract_process_tree(self, file_path: str) -> list[dict]:
        output_file = self.run_volatility(
            file_path,
            "windows.pstree",
            "process_tree.txt"
        )
        parsed = self.parser.parse_pslist(output_file)
        return parsed


    def extract_process_hidden(self, file_path: str) -> list[dict]:
        output_file = self.run_volatility(
            file_path,
            "windows.psxview",
            "process_psxview.txt"
        )
        parsed = self.parser.parse_pslist(output_file)
        return parsed


    def extract_process_command_line_args(self, file_path: str) -> list[dict]:
        output_file = self.run_volatility(
            file_path,
            "windows.cmdline",
            "process_cmdline.txt"
        )
        parsed = self.parser.parse_pslist(output_file)
        return parsed


    def extract_process_environment_vars(self, file_path: str) -> list[dict]:
        output_file = self.run_volatility(
            file_path,
            "windows.envars",
            "process_envars.txt"
        )
        parsed = self.parser.parse_pslist(output_file)
        return parsed

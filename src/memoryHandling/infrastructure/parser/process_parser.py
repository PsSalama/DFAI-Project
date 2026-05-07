import re
from src.memoryHandling.infrastructure.mappers.process_mapper_vol_dict import *

class ProcessParser:
    @staticmethod
    def process_parse(file_path: str) -> list[dict]:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = [l.strip() for l in f.readlines() if l.strip()]

        header_index = None
        for i, line in enumerate(lines):
            if line.startswith("PID"):
                header_index = i
                break

        if header_index is None:
            raise ValueError("Header not found")

        header_line = lines[header_index]
        headers = re.split(r"\t+", header_line)
        data = []
        for line in lines[header_index + 1:]:
            values = re.split(r"\t+", line)
            if len(values) != len(headers):
                continue
            row = dict(zip(headers, values))
            #mapped_row = ProcessListMapperToDict.vol_to_dict(row)
            data.append(row)
        return data
import re
from src.memoryHandling.infrastructure.mappers.process_mapper_vol_dict import *

class ProcessListParser:
    def parse_pslist(self, file_path: str) -> list[dict]:
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
        mapper = ProcessListMapperToDict()
        data = []
        for line in lines[header_index + 1:]:
            values = re.split(r"\t+", line)
            if len(values) != len(headers):
                continue
            row = dict(zip(headers, values))
            print(row.get("File output"))
            mapped_row = mapper.vol_to_dict(row)
            data.append(mapped_row)
        return data

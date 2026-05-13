from src.memoryHandling.app.ports.process.i_data_parsing import IDataParsing
from src.memoryHandling.infrastructure.parsers.process_parser import ProcessParser
from src.memoryHandling.infrastructure.mappers.process_mapper_vol_dict import *


class ImpDataParsing(IDataParsing):
    def parse_data(self, raw_file: str) -> list[dict]:
        data_parsed = ProcessParser.process_parse(raw_file)
        data_mapped = [
            ProcessListMapperToDict.vol_to_dict(process)
            for process in data_parsed
        ]
        return data_mapped

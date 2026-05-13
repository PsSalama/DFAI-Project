from abc import ABC, abstractmethod


class IDataParsing(ABC):
    @abstractmethod
    def parse_data(self, raw_file: str)-> list[dict]:
        pass
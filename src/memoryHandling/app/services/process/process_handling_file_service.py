from src.memoryHandling.app.ports.process.i_data_parsing import IDataParsing
from src.memoryHandling.app.ports.process.i_process_repo import IProcessRepo


class ProcessHandlingFileService:
    def __init__(self, parsing: IDataParsing, repo: IProcessRepo) -> None:
        self.parsing = parsing
        self.repo = repo


    async def parse_process_file(self, out_file: str) -> list[dict]:
        return self.parsing.parse_data(out_file)


    async def store_data(self, raw_data: list[dict]) -> list[dict]:
        return self.repo.store_process_list("12324", "memory", raw_data)

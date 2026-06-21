from src.memoryEngine.internal.app.ports.file.i_file_repo import IFileRepo


class FileStoreService:
    def __init__(self, repo: IFileRepo):
        self.repo = repo


    def store_file_scan(self, parsed_data: list[dict]):
        self.repo.store_file_scan(parsed_data)


    def store_file_dump(self, parsed_data: list[dict]):
        self.repo.store_file_dump(parsed_data)
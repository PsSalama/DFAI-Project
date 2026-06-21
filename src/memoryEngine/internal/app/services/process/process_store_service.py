from src.memoryEngine.internal.app.ports.process.i_process_repo import IProcessRepo


class ProcessStoreService:
    def __init__(self, repo: IProcessRepo):
        self.repo = repo


    def store(self, parsed_data: list[dict]):
        self.repo.store_process_xview(parsed_data)
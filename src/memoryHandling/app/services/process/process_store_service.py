from src.memoryHandling.app.ports.process.i_process_repo import IProcessRepo


class ProcessStoreService:
    def __init__(self, repo: IProcessRepo):
        self.repo = repo


    def store(self, parsed_data: list[dict]):
        self.repo.store_process_list("123455","memory", parsed_data)
from src.memoryEngine.internal.app.ports.process.i_process_repo import IProcessRepo


class ProcessStoreService:
    def __init__(self, repo: IProcessRepo):
        self.repo = repo


    def store_process_view(self, parsed_data: list[dict]):
        self.repo.store_process_view(parsed_data)


    def store_process_list(self, parsed_data: list[dict]):
        self.repo.store_process_list(parsed_data)


    def store_process_scan(self, parsed_data: list[dict]):
        self.repo.store_process_scan(parsed_data)

    def store_process_tree(self, parsed_data: list[dict]):
        self.repo.store_process_tree(parsed_data)
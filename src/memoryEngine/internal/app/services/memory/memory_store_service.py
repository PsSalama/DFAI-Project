from src.memoryEngine.internal.app.ports.memory.i_memory_repo import IMemoryRepo


class MemoryStoreService:
    def __init__(self, repo: IMemoryRepo):
        self.repo = repo


    def store_memory_info(self, parsed_data: dict):
        self.repo.store_memory_info(parsed_data)
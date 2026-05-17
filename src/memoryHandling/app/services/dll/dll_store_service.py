from src.memoryHandling.app.ports.dll.i_dll_repo import IDllRepo


class DllStoreService:
    def __init__(self, repo: IDllRepo):
        self.repo = repo


    def store_dll_list(self, parsed_data: list[dict]):
        self.repo.store_dll_list(parsed_data)


    def store_dll_ldrmodules(self, parsed_data: list[dict]):
        self.repo.store_dll_ldrmodule(parsed_data)


    def store_dll_module(self, parsed_data: list[dict]):
        self.repo.store_dll_module(parsed_data)


    def store_dll_modscan(self, parsed_data: list[dict]):
        self.repo.store_dll_modscan(parsed_data)
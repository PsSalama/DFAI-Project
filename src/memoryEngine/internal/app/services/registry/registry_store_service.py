from src.memoryEngine.internal.app.ports.registry.i_registry_repo import IRegistryRepo


class RegistryStoreService:
    def __init__(self, repo: IRegistryRepo):
        self.repo = repo


    def store_registry_list(self, parsed_data: list[dict]):
        self.repo.store_registry_list(parsed_data)


    def store_registry_scan(self, parsed_data: list[dict]):
        self.repo.store_registry_scan(parsed_data)


    def store_registry_key(self, parsed_data: list[dict]):
        self.repo.store_registry_key(parsed_data)


    def store_registry_cert(self, parsed_data: list[dict]):
        self.repo.store_registry_cert(parsed_data)
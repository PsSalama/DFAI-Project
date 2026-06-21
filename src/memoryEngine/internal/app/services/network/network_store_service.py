from src.memoryEngine.internal.app.ports.network.i_network_repo import INetworkRepo


class NetworkStoreService:
    def __init__(self, repo: INetworkRepo):
        self.repo = repo


    def store_network_scan(self, parsed_data: list[dict]):
        self.repo.store_network_scan(parsed_data)


    def store_network_stat(self, parsed_data: list[dict]):
        self.repo.store_network_stat(parsed_data)
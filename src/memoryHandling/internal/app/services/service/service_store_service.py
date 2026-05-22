from src.memoryHandling.internal.app.ports.service.i_service_repo import IServiceRepo


class ServiceStoreService:
    def __init__(self, repo: IServiceRepo):
        self.repo = repo


    def store_service_scan(self, parsed_data: list[dict]):
        self.repo.store_service_scan(parsed_data)
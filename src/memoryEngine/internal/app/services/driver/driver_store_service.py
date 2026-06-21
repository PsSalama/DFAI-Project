from src.memoryEngine.internal.app.ports.driver.i_driver_repo import IDriverRepo


class DriverStoreService:
    def __init__(self, repo: IDriverRepo):
        self.repo = repo


    def store_driver_scan(self, parsed_data: list[dict]):
        self.repo.store_driver_scan(parsed_data)


    def store_driver_irp(self, parsed_data: list[dict]):
        self.repo.store_driver_irp(parsed_data)
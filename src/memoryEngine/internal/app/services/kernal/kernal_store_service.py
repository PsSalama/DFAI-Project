from src.memoryEngine.internal.app.ports.kernal.i_kernal_repo import IKernalRepo


class KernalStoreService:
    def __init__(self, repo: IKernalRepo):
        self.repo = repo


    def store_ssdt(self, parsed_data: list[dict]):
        self.repo.store_ssdt(parsed_data)

from src.memoryEngine.internal.app.ports.handle.i_handle_repo import IHandleRepo


class HandleStoreService:
    def __init__(self, repo: IHandleRepo):
        self.repo = repo


    def store_handle(self, parsed_data: list[dict]):
        self.repo.store_handle(parsed_data)

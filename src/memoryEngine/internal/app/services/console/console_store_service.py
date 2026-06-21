from src.memoryEngine.internal.app.ports.console.i_console_repo import IConsoleRepo


class ConsoleStoreService:
    def __init__(self, repo: IConsoleRepo):
        self.repo = repo


    def store_console(self, parsed_data: list[dict]):
        self.repo.store_console(parsed_data)


    def store_console_cmdscan(self, parsed_data: list[dict]):
        self.repo.store_console_cmdscan(parsed_data)

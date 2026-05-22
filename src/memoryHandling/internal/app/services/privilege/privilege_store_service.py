from src.memoryHandling.internal.app.ports.privilege.i_privilege_repo import IPrivilegeRepo


class PrivilegeStoreService:
    def __init__(self, repo: IPrivilegeRepo):
        self.repo = repo


    def store_privilege_process(self, parsed_data: list[dict]):
        self.repo.store_privilege_process(parsed_data)


    def store_privilege_service_id(self, parsed_data: list[dict]):
        self.repo.store_privilege_service_id(parsed_data)
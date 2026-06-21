from abc import ABC, abstractmethod


class IPrivilegeRepo(ABC):
    @abstractmethod
    def store_privilege_process(self, privilege_process: list[dict]):
        pass


    @abstractmethod
    def store_privilege_service_id(self, privilege_service_id: list[dict]):
        pass
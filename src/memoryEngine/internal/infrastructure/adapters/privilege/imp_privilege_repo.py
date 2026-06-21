from config.database import Database
from src.memoryEngine.internal.app.ports.privilege.i_privilege_repo import IPrivilegeRepo
from src.memoryEngine.internal.infrastructure.mappers.privilege_dict_to_database import *


class ImpPrivilegeRepo(IPrivilegeRepo):
    def store_privilege_process(self, privilege_process: list[dict]):
        if not privilege_process:
            return
        documents = [ PrivilegeProcessMapperToDatabaseModel.dict_to_database(p) for p in privilege_process ]
        Database.db["privileges"].insert_many(documents)


    def store_privilege_service_id(self, privilege_service_id: list[dict]):
        if not privilege_service_id:
            return
        documents = [ PrivilegeServiceIdMapperToDatabaseModel.dict_to_database(p) for p in privilege_service_id ]
        Database.db["privileges"].insert_many(documents)
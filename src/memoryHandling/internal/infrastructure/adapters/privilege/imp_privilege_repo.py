from config.database import Database
from src.memoryHandling.internal.app.ports.privilege.i_privilege_repo import IPrivilegeRepo
from src.memoryHandling.internal.infrastructure.mappers.privilege_dict_to_database import *


class ImpPrivilegeRepo(IPrivilegeRepo):
    def store_privilege_process(self, privilege_process: list[dict]):
        documents = [ PrivilegeProcessMapperToDatabaseModel.dict_to_database(p) for p in privilege_process ]
        Database.db["privileges"].insert_many(documents)


    def store_privilege_service_id(self, privilege_service_id: list[dict]):
        documents = [ PrivilegeServiceIdMapperToDatabaseModel.dict_to_database(p) for p in privilege_service_id ]
        Database.db["privileges"].insert_many(documents)
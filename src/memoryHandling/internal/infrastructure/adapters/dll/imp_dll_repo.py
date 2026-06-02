from config.database import Database
from src.memoryHandling.internal.app.ports.dll.i_dll_repo import IDllRepo
from src.memoryHandling.internal.infrastructure.mappers.dll_dict_to_database import *


class ImpDllRepo(IDllRepo):
    def store_dll_list(self, dlls_list: list[dict]):
        if not dlls_list:
            return
        documents = [ DllListMapperToDatabaseModel.dict_to_database(p) for p in dlls_list ]
        Database.db["dlls"].insert_many(documents)


    def store_dll_ldrmodule(self, dlls_ldrmodule: list[dict]):
        if not dlls_ldrmodule:
            return
        documents = [ DllLdrmodulesMapperToDatabaseModel.dict_to_database(p) for p in dlls_ldrmodule ]
        Database.db["dlls"].insert_many(documents)


    def store_dll_module(self, dlls_module: list[dict]):
        if not dlls_module:
            return
        documents = [ DllModuleMapperToDatabaseModel.dict_to_database(p) for p in dlls_module ]
        Database.db["dlls"].insert_many(documents)


    def store_dll_modscan(self, dlls_modscan: list[dict]):
        if not dlls_modscan:
            return
        documents = [ DllModscanMapperToDatabaseModel.dict_to_database(p) for p in dlls_modscan ]
        Database.db["dlls"].insert_many(documents)
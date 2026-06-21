from config.database import Database
from src.memoryEngine.internal.app.ports.registry.i_registry_repo import IRegistryRepo
from src.memoryEngine.internal.infrastructure.mappers.registry_dict_to_database import *


class ImpRegistryRepo(IRegistryRepo):
    def store_registry_list(self, registry_list: list[dict]):
        if not registry_list:
            return
        documents = [RegistryListMapperToDatabaseModel.dict_to_database(p) for p in registry_list]
        Database.db["registries"].insert_many(documents)


    def store_registry_scan(self, registry_scan: list[dict]):
        if not registry_scan:
            return
        documents = [RegistryScanMapperToDatabaseModel.dict_to_database(p) for p in registry_scan]
        Database.db["registries"].insert_many(documents)


    def store_registry_key(self, registry_key: list[dict]):
        if not registry_key:
            return
        documents = [RegistryKeyMapperToDatabaseModel.dict_to_database(p) for p in registry_key]
        Database.db["registries"].insert_many(documents)


    def store_registry_cert(self, registry_cert: list[dict]):
        if not registry_cert:
            return
        documents = [RegistryCertMapperToDatabaseModel.dict_to_database(p) for p in registry_cert]
        Database.db["registries"].insert_many(documents)
from config.database import Database
from src.memoryHandling.app.ports.registry.i_registry_repo import IRegistryRepo
from src.memoryHandling.infrastructure.mappers.registry_dict_to_database import *


class ImpRegistryRepo(IRegistryRepo):
    def store_registry_list(self, registry_list: list[dict]):
        documents = [RegistryListMapperToDatabaseModel.dict_to_database(p) for p in registry_list]
        Database.db["registries"].insert_many(documents)


    def store_registry_scan(self, registry_scan: list[dict]):
        documents = [RegistryScanMapperToDatabaseModel.dict_to_database(p) for p in registry_scan]
        Database.db["registries"].insert_many(documents)


    def store_registry_key(self, registry_key: list[dict]):
        documents = [RegistryKeyMapperToDatabaseModel.dict_to_database(p) for p in registry_key]
        Database.db["registries"].insert_many(documents)


    def store_registry_cert(self, registry_cert: list[dict]):
        documents = [RegistryCertMapperToDatabaseModel.dict_to_database(p) for p in registry_cert]
        Database.db["registries"].insert_many(documents)
from config.database import Database
from src.memoryHandling.internal.app.ports.network.i_network_repo import INetworkRepo
from src.memoryHandling.internal.infrastructure.mappers.network_dict_to_database import *


class ImpNetworkRepo(INetworkRepo):
    def store_network_scan(self, network_scan: list[dict]):
        documents = [NetworkScanMapperToDatabaseModel.dict_to_database(p) for p in network_scan]
        Database.db["network"].insert_many(documents)


    def store_network_stat(self, network_stat: list[dict]):
        documents = [NetworkStatMapperToDatabaseModel.dict_to_database(p) for p in network_stat]
        Database.db["network"].insert_many(documents)
from config.database import Database
from src.memoryEngine.internal.app.ports.process.i_process_repo import IProcessRepo
from src.memoryEngine.internal.infrastructure.mappers.process_dict_to_database import *


class ImpProcessRepo(IProcessRepo):
    def store_process_view(self, processes_view: list[dict]):
        if not processes_view:
            return
        documents = [ ProcessViewMapperToDatabaseModel.dict_to_database(p) for p in processes_view ]
        Database.db["processes"].insert_many(documents)


    def store_process_list(self, processes_list: list[dict]):
        if not processes_list:
            return
        documents = [ ProcessListMapperToDatabaseModel.dict_to_database(p) for p in processes_list ]
        Database.db["processes"].insert_many(documents)


    def store_process_scan(self, processes_scan: list[dict]):
        if not processes_scan:
            return
        documents = [ ProcessScanMapperToDatabaseModel.dict_to_database(p) for p in processes_scan ]
        Database.db["processes"].insert_many(documents)


    def store_process_tree(self, processes_tree: list[dict]):
        if not processes_tree:
            return
        documents = [ ProcessTreeMapperToDatabaseModel.dict_to_database(p) for p in processes_tree ]
        Database.db["processes"].insert_many(documents)


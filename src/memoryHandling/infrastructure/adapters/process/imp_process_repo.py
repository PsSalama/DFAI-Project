from config.database import Database
from src.memoryHandling.app.ports.process.i_process_repo import IProcessRepo
from src.memoryHandling.infrastructure.mappers.process_dict_to_database import *


class ImpProcessRepo(IProcessRepo):
    def store_process_list(self, processes_list: list[dict]):
        documents = [ ProcessListMapperToDatabaseModel.dict_to_database(p) for p in processes_list ]
        Database.db["processes"].insert_many(documents)


    def store_process_xview(self, processes_xview: list[dict]):
        documents = [ ProcessXviewMapperToDatabaseModel.dict_to_database(p) for p in processes_xview ]
        Database.db["processes"].insert_many(documents)


    def store_process_tree(self, processes_tree: list[dict]):
        documents = [ ProcessTreeMapperToDatabaseModel.dict_to_database(p) for p in processes_tree ]
        Database.db["processes"].insert_many(documents)


    def store_process_hidden(self, processes_hidden: list[dict]):
        documents = [ ProcessHiddenMapperToDatabaseModel.dict_to_database(p) for p in processes_hidden ]
        Database.db["processes"].insert_many(documents)


    def store_process_command_line(self, processes_cmd: list[dict]):
        documents = [ ProcessCommandLineMapperToDatabaseModel.dict_to_database(p) for p in processes_cmd ]
        Database.db["processes"].insert_many(documents)


    def store_process_environment_vars(self, processes_env: list[dict]):
        documents = [ ProcessEnvironmentVarsMapperToDatabaseModel.dict_to_database(p) for p in processes_env ]
        Database.db["processes"].insert_many(documents)

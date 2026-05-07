from config.database import Database
from src.memoryHandling.app.ports.database.i_process_repo import IProcessRepo
from src.memoryHandling.infrastructure.mappers.process_mapper_dict_database import *


class ImpProcessRepo(IProcessRepo):
    def store_process_list(self, processes_list: list[dict]):
        db_models = [ ProcessListMapperToDatabaseModel.dict_to_database(p) for p in processes_list ]
        documents = [ model.model_dump() for model in db_models ]
        Database.db["processes_list"].insert_many(documents)


    def store_process_tree(self, processes_tree: list[dict]):
        db_models = [ ProcessTreeMapperToDatabaseModel.dict_to_database(p) for p in processes_tree ]
        documents = [ model.model_dump() for model in db_models ]
        Database.db["processes_tree"].insert_many(documents)


    def store_process_hidden(self, processes_hidden: list[dict]):
        db_models = [ ProcessHiddenMapperToDatabaseModel.dict_to_database(p) for p in processes_hidden ]
        documents = [ model.model_dump() for model in db_models ]
        Database.db["processes_hidden"].insert_many(documents)


    def store_process_command_line(self, processes_cmd: list[dict]):
        db_models = [ ProcessCommandLineMapperToDatabaseModel.dict_to_database(p) for p in processes_cmd ]
        documents = [ model.model_dump() for model in db_models ]
        Database.db["processes_cmdline"].insert_many(documents)


    def store_process_environment_vars(self, processes_env: list[dict]):
        db_models = [ ProcessEnvironmentVarsMapperToDatabaseModel.dict_to_database(p) for p in processes_env ]
        documents = [ model.model_dump() for model in db_models ]
        Database.db["processes_env"].insert_many(documents)

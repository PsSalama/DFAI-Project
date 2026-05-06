from config.database import Database
from src.memoryHandling.app.ports.database.i_process_repo import IProcessRepo
from src.memoryHandling.infrastructure.mappers.process_mapper_dict_database import *


class ImpProcessRepo(IProcessRepo):
    def store_process_list(self, processes_list: list[dict]):
        mapper = ProcessListMapperToDatabaseModel()
        db_models = [ mapper.dict_to_database(p) for p in processes_list ]
        documents = [ model.model_dump() for model in db_models ]
        Database.db["processes_list"].insert_many(documents)


    def store_process_tree(self, processes_tree: list[dict]):
        mapper = ProcessTreeMapperToDatabaseModel()
        db_models = [ mapper.dict_to_database(p) for p in processes_tree ]
        documents = [ model.model_dump() for model in db_models ]
        Database.db["processes_tree"].insert_many(documents)


    def store_process_hidden(self, processes_hidden: list[dict]):
        mapper = ProcessHiddenMapperToDatabaseModel()
        db_models = [ mapper.dict_to_database(p) for p in processes_hidden ]
        documents = [ model.model_dump() for model in db_models ]
        Database.db["processes_hidden"].insert_many(documents)


    def store_process_command_line(self, processes_cmd: list[dict]):
        mapper = ProcessCommandLineMapperToDatabaseModel()
        db_models = [ mapper.dict_to_database(p) for p in processes_cmd ]
        documents = [ model.model_dump() for model in db_models ]
        Database.db["processes_cmdline"].insert_many(documents)


    def store_process_environment_vars(self, processes_env: list[dict]):
        mapper = ProcessEnvironmentVarsMapperToDatabaseModel()
        db_models = [ mapper.dict_to_database(p) for p in processes_env ]
        documents = [ model.model_dump() for model in db_models ]
        Database.db["processes_env"].insert_many(documents)

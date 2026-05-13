from config.database import Database
from ports.process.i_process_repo import IProcessRepo
from src.memoryHandling.infrastructure.mappers.process_mapper_dict_database import *


class ImpProcessRepo(IProcessRepo):
    def store_process_list(self, project_id: str, source_type: str, processes_list: list[dict]):
        db_models = [ ProcessListMapperToDatabaseModel.dict_to_database(project_id, source_type, p) for p in processes_list ]
        documents = [ model.model_dump() for model in db_models ]
        Database.db[project_id+"_"+source_type+"_processes"].insert_many(documents)


    def store_process_tree(self, project_id: str, source_type: str, processes_tree: list[dict]):
        db_models = [ ProcessTreeMapperToDatabaseModel.dict_to_database(project_id, source_type, p) for p in processes_tree ]
        documents = [ model.model_dump() for model in db_models ]
        Database.db[project_id+"_"+source_type+"_processes"].insert_many(documents)


    def store_process_hidden(self, project_id: str, source_type: str, processes_hidden: list[dict]):
        db_models = [ ProcessHiddenMapperToDatabaseModel.dict_to_database(project_id, source_type, p) for p in processes_hidden ]
        documents = [ model.model_dump() for model in db_models ]
        Database.db[project_id+"_"+source_type+"_processes"].insert_many(documents)


    def store_process_command_line(self, project_id: str, source_type: str, processes_cmd: list[dict]):
        db_models = [ ProcessCommandLineMapperToDatabaseModel.dict_to_database(project_id, source_type, p) for p in processes_cmd ]
        documents = [ model.model_dump() for model in db_models ]
        Database.db[project_id+"_"+source_type+"_processes"].insert_many(documents)


    def store_process_environment_vars(self, project_id: str, source_type: str, processes_env: list[dict]):
        db_models = [ ProcessEnvironmentVarsMapperToDatabaseModel.dict_to_database(project_id, source_type, p) for p in processes_env ]
        documents = [ model.model_dump() for model in db_models ]
        Database.db[project_id+"_"+source_type+"_processes"].insert_many(documents)

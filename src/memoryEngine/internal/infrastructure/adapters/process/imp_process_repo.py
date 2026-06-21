from config.database import Database
from src.memoryEngine.internal.app.ports.process.i_process_repo import IProcessRepo
from src.memoryEngine.internal.infrastructure.mappers.process_dict_to_database import *


class ImpProcessRepo(IProcessRepo):
    # def store_process_list(self, processes_list: list[dict]):
    #     if not processes_list:
    #         return
    #     documents = [ ProcessListMapperToDatabaseModel.dict_to_database(p) for p in processes_list ]
    #     Database.db["processes"].insert_many(documents)


    def store_process_xview(self, processes_xview: list[dict]):
        if not processes_xview:
            return
        documents = [ ProcessXviewMapperToDatabaseModel.dict_to_database(p) for p in processes_xview ]
        Database.db["processes"].insert_many(documents)


    # def store_process_tree(self, processes_tree: list[dict]):
    #     if not processes_tree:
    #         return
    #     documents = [ ProcessTreeMapperToDatabaseModel.dict_to_database(p) for p in processes_tree ]
    #     Database.db["processes"].insert_many(documents)
    #
    #
    # def store_process_hidden(self, processes_hidden: list[dict]):
    #     if not processes_hidden:
    #         return
    #     documents = [ ProcessHiddenMapperToDatabaseModel.dict_to_database(p) for p in processes_hidden ]
    #     Database.db["processes"].insert_many(documents)
    #
    #
    # def store_process_command_line(self, processes_cmd: list[dict]):
    #     if not processes_cmd:
    #         return
    #     documents = [ ProcessCommandLineMapperToDatabaseModel.dict_to_database(p) for p in processes_cmd ]
    #     Database.db["processes"].insert_many(documents)
    #
    #
    # def store_process_environment_vars(self, processes_env: list[dict]):
    #     if not processes_env:
    #         return
    #     documents = [ ProcessEnvironmentVarsMapperToDatabaseModel.dict_to_database(p) for p in processes_env ]
    #     Database.db["processes"].insert_many(documents)

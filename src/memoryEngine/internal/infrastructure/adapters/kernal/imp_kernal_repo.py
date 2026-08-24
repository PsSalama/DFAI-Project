from config.database import Database
from src.memoryEngine.internal.app.ports.kernal.i_kernal_repo import IKernalRepo
from src.memoryEngine.internal.infrastructure.mappers.kernal_dict_to_database import *


class ImpKernalRepo(IKernalRepo):
    def store_ssdt(self, ssdt: list[dict]):
        if not ssdt:
            return
        documents = [ kernalMapperToDatabaseModel.dict_to_database(p) for p in ssdt ]
        Database.db["kernal"].insert_many(documents)
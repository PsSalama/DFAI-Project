from config.database import Database
from src.memoryHandling.internal.app.ports.memory.i_memory_repo import IMemoryRepo
from src.memoryHandling.internal.infrastructure.mappers.memory_dict_to_database import *


class ImpMemoryRepo(IMemoryRepo):
    def store_memory_info(self, memory_info: list[dict]):
        documents = [ MemoryInfoMapperToDatabaseModel.dict_to_database(p) for p in memory_info ]
        Database.db["memory"].insert_many(documents)
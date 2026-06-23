from config.database import Database
from src.memoryEngine.internal.app.ports.handle.i_handle_repo import IHandleRepo
from src.memoryEngine.internal.infrastructure.mappers.handle_dict_to_database import *


class ImpHandleRepo(IHandleRepo):
    def store_handle(self, handles: list[dict]):
        if not handles:
            return
        documents = [ HandleMapperToDatabaseModel.dict_to_database(p) for p in handles ]
        Database.db["handles"].insert_many(documents)
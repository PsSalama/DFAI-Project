from config.database import Database
from src.memoryEngine.internal.app.ports.file.i_file_repo import IFileRepo
from src.memoryEngine.internal.infrastructure.mappers.file_dict_to_database import *


class ImpFileRepo(IFileRepo):
    def store_file_scan(self, file_scan: list[dict]):
        if not file_scan:
            return
        documents = [ FileScanMapperToDatabaseModel.dict_to_database(p) for p in file_scan ]
        Database.db["files"].insert_many(documents)


    def store_file_dump(self, file_dump: list[dict]):
        if not file_dump:
            return
        documents = [ FileDumpMapperToDatabaseModel.dict_to_database(p) for p in file_dump ]
        Database.db["files"].insert_many(documents)
from config.database import Database
from src.memoryHandling.internal.app.ports.service.i_service_repo import IServiceRepo
from src.memoryHandling.internal.infrastructure.mappers.service_dict_to_database import *


class ImpServiceRepo(IServiceRepo):
    def store_service_scan(self, service_scan: list[dict]):
        if not service_scan:
            return
        documents = [ServiceScanMapperToDatabaseModel.dict_to_database(p) for p in service_scan]
        Database.db["services"].insert_many(documents)
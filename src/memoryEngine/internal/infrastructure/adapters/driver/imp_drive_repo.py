from config.database import Database
from src.memoryEngine.internal.app.ports.driver.i_driver_repo import IDriverRepo
from src.memoryEngine.internal.infrastructure.mappers.driver_dict_to_database import *


class ImpDriverRepo(IDriverRepo):
    def store_driver_scan(self, driver_scan: list[dict]):
        if not driver_scan:
            return
        documents = [ DriverScanMapperToDatabaseModel.dict_to_database(p) for p in driver_scan ]
        Database.db["drivers"].insert_many(documents)


    def store_driver_irp(self, driver_irp: list[dict]):
        if not driver_irp:
            return
        documents = [ DriverIrpMapperToDatabaseModel.dict_to_database(p) for p in driver_irp ]
        Database.db["drivers"].insert_many(documents)
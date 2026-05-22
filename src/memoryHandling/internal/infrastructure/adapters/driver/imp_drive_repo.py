from config.database import Database
from src.memoryHandling.internal.app.ports.driver.i_driver_repo import IDriverRepo
from src.memoryHandling.internal.infrastructure.mappers.driver_dict_to_database import *


class ImpDriverRepo(IDriverRepo):
    def store_driver_scan(self, driver_scan: list[dict]):
        documents = [ DriverScanMapperToDatabaseModel.dict_to_database(p) for p in driver_scan ]
        Database.db["drivers"].insert_many(documents)


    def store_driver_irp(self, driver_irp: list[dict]):
        documents = [ DriverIrpMapperToDatabaseModel.dict_to_database(p) for p in driver_irp ]
        Database.db["drivers"].insert_many(documents)
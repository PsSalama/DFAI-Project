from config.database import Database
from src.memoryHandling.internal.app.ports.console.i_console_repo import IConsoleRepo
from src.memoryHandling.internal.infrastructure.mappers.console_dict_to_database import *


class ImpConsoleRepo(IConsoleRepo):
    def store_console(self, console: list[dict]):
        if not console:
            return
        documents = [ ConsoleMapperToDatabaseModel.dict_to_database(p) for p in console ]
        Database.db["consoles"].insert_many(documents)


    def store_console_cmdscan(self, console_cmdscan: list[dict]):
        if not console_cmdscan:
            return
        documents = [ ConsoleCmdScanMapperToDatabaseModel.dict_to_database(p) for p in console_cmdscan ]
        Database.db["consoles"].insert_many(documents)

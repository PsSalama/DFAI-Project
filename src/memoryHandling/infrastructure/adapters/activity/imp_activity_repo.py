from config.database import Database
from src.memoryHandling.app.ports.activity.i_activity_repo import IActivityRepo
from src.memoryHandling.infrastructure.mappers.activity_dict_to_database import *


class ImpActivityRepo(IActivityRepo):
    def store_activity_session(self, activity_session: list[dict]):
        documents = [ ActivitySessionMapperToDatabaseModel.dict_to_database(p) for p in activity_session ]
        Database.db["activities"].insert_many(documents)


    def store_activity_sid(self, activity_sid: list[dict]):
        documents = [ ActivitySidMapperToDatabaseModel.dict_to_database(p) for p in activity_sid ]
        Database.db["activities"].insert_many(documents)


    def store_activity_desktop(self, activity_desktop: list[dict]):
        documents = [ ActivityDesktopMapperToDatabaseModel.dict_to_database(p) for p in activity_desktop ]
        Database.db["activities"].insert_many(documents)

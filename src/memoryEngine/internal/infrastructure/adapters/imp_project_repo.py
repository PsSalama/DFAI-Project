from config.database import Database
from pathlib import Path
import shutil
import redis
from src.memoryEngine.internal.app.ports.i_project_repo import IProjectRepo

class ImpProjectRepo(IProjectRepo):
    def delete_project(self):
        for collection_name in Database.db.list_collection_names():
            Database.db.drop_collection(collection_name)

        # Delete dumps directory
        dumps_dir = Path("dumps")
        if dumps_dir.exists() and dumps_dir.is_dir():
            shutil.rmtree(dumps_dir)

        # Clear broker
        redis.Redis(host="localhost", port=6379, db=0).flushdb()

        # Clear result backend
        redis.Redis(host="localhost", port=6379, db=1).flushdb()

        # Clear result backend
        redis.Redis(host="localhost", port=6379, db=2).flushdb()
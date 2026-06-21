from src.memoryEngine.internal.app.ports.activity.i_activity_repo import IActivityRepo


class ActivityStoreService:
    def __init__(self, repo: IActivityRepo):
        self.repo = repo


    def store_activity_session(self, parsed_data: list[dict]):
        self.repo.store_activity_session(parsed_data)


    def store_activity_sid(self, parsed_data: list[dict]):
        self.repo.store_activity_sid(parsed_data)


    def store_activity_desktop(self, parsed_data: list[dict]):
        self.repo.store_activity_desktop(parsed_data)

from abc import ABC, abstractmethod


class IActivityRepo(ABC):
    @abstractmethod
    def store_activity_session(self, activity_session: list[dict]):
        pass


    @abstractmethod
    def store_activity_sid(self, activity_sid: list[dict]):
        pass


    @abstractmethod
    def store_activity_desktop(self, activity_desktop: list[dict]):
        pass

from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def save_metadata_to_db(self, *args, **kwargs):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass

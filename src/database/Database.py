from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def save_footage(self, footage_stream, filename: str):
        pass

    @abstractmethod
    def close(self):
        pass

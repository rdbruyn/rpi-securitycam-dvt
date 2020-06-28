from abc import ABC, abstractmethod


class Runner(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def should_run(self):
        pass

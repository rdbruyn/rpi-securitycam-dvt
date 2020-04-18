from abc import ABC, abstractmethod


class MotionCamera(ABC):
    @abstractmethod
    def capture_next_image(self):
        pass

from abc import ABC, abstractmethod
import numpy as np
import io


class MotionCamera(ABC):
    @abstractmethod
    def capture_next_image(self) -> np.ndarray:
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def start_recording(self):
        pass

    @abstractmethod
    def stop_recording(self):
        pass

    @property
    @abstractmethod
    def is_recording(self) -> bool:
        pass

    @abstractmethod
    def get_video_stream(self) -> io.BytesIO:
        pass

    @abstractmethod
    def wait_recording(self, wait_time: float):
        pass

    @abstractmethod
    def start_preview(self):
        pass

    @abstractmethod
    def stop_preview(self):
        pass

    @abstractmethod
    def annotate(self):
        pass

    @abstractmethod
    def __init__(self, json_args=None):
        pass

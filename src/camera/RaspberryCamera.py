import io
import numpy as np
from picamera import PiCamera

from .MotionCamera import MotionCamera


class RaspberryCamera(MotionCamera):
    def capture_next_image(self) -> np.ndarray:
        img = np.empty((480, 640, 3), dtype=np.uint8)
        img = self.camera.capture(img, 'rgb', use_video_port=True)
        return img

    def close(self):
        self.camera.close()

    def start_recording(self):
        self.video_stream = io.BytesIO
        self.camera.start_recording(self.video_stream, format='h264', quality=20)

    def stop_recording(self):
        self.camera.stop_recording()

    @property
    def is_recording(self) -> bool:
        return self.camera.recording

    def get_video_stream(self) -> io.BytesIO:
        return self.video_stream

    def wait_recording(self, wait_time: float):
        self.camera.wait_recording(wait_time)

    def start_preview(self):
        self.camera.start_preview()

    def stop_preview(self):
        self.camera.stop_preview()

    def __init__(self, json_args=None):
        super().__init__(json_args)
        self.camera = PiCamera(sensor_mode=7)
        self.video_stream = io.BytesIO()

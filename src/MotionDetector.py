import numpy as np
from camera.MotionCamera import MotionCamera
from Database import Database
from runner.Runner import Runner

import io
import time
import asyncio
from typing import Optional
from ffmpeg import FFmpeg


class MotionDetector:
    def __init__(
            self,
            camera: Optional[MotionCamera] = None,
            database: Optional[Database] = None,
            runner: Optional[Runner] = None,
            active_ratio=.01,
            inactive_ratio=.03,
            threshold=15
    ):
        self.camera = camera
        self.database = database
        self.runner = runner
        self.active_ratio = active_ratio
        self.inactive_ratio = inactive_ratio
        self.threshold = threshold

        self.stop_signal = False
        self.output_directory = '/home/pi/Videos'
        self.diff_ratio = 0

    def test_for_motion(self, image1: np.ndarray, image2: np.ndarray, ratio: float) -> bool:
        grayscale_map_vector = np.asarray([.2989, .587, .114])
        gray1 = np.dot(image1[...,:3], grayscale_map_vector)
        gray2 = np.dot(image2[...,:3], grayscale_map_vector)
        bool_image = np.abs(
            gray1.astype(np.int16) - gray2.astype(np.int16)
        ) > self.threshold

        total_pixels = image1.shape[0] * image1.shape[1]
        diff_ratio = np.sum(bool_image) / total_pixels
        self.diff_ratio = diff_ratio
        return diff_ratio > ratio

    def print_movement_logs(self, ratio):
        print(
            'Difference ratio:  {}\n'
            'Tested for ratio: {}'
            .format(self.diff_ratio, ratio)
        )

    def stop(self):
        self.stop_signal = True

    def run(self):
        self.runner.start()

        on_cooldown = True

        image_pair = [None, self.camera.capture_next_image()]

        while self.runner.should_run():
            image_pair[0] = image_pair[1]
            image_pair[1] = self.camera.capture_next_image()
            if self.camera.is_recording:
                motion_confirmed = self.test_for_motion(image_pair[0], image_pair[1], self.active_ratio)
                self.print_movement_logs(self.active_ratio)
                if motion_confirmed:
                    print('Motion confirmed')
                    on_cooldown = True
                elif on_cooldown:
                    self.camera.wait_recording(2)
                    on_cooldown = False
                else:
                    print('Movement stopped and cooldown period expired. Saving video file.')
                    self.camera.stop_recording()
                    recorded_stream = self.camera.get_video_stream()
                    timestamp = time.strftime("%Y%m%d-%H %M %S")
                    filename = '{}/{}.h264'.format(self.output_directory, timestamp)
                    output = io.open('{}/{}.h264'.format(self.output_directory, timestamp), 'wb')
                    output.write(recorded_stream.getvalue())
                    output.close()
                    ffmpeg = FFmpeg().input(filename).output('/home/pi/Videos/test.mp4')
                    t1 = time.time()
                    loop = asyncio.get_event_loop()
                    loop.run_until_complete(ffmpeg.execute())
                    loop.close()
                    t2 = time.time()
                    print('ffmpeg time to encode: {}'.format(t2 - t1))
                    time.sleep(1)
            else:
                motion_confirmed = self.test_for_motion(image_pair[0], image_pair[1], self.inactive_ratio)
                self.print_movement_logs(self.inactive_ratio)
                if motion_confirmed:
                    self.camera.start_recording()
                    self.camera.start_preview()
                    on_cooldown = True
                else:
                    continue

        self.camera.close()

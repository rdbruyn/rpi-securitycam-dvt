from MotionDetector import MotionDetector
from camera.RaspberryCamera import RaspberryCamera
from runner.TimeRunner import TimeRunner
from time import sleep

if __name__ == '__main__':
    cam = RaspberryCamera()
    sleep(1)
    runner = TimeRunner(10)
    detector = MotionDetector(cam, None, runner)
    detector.run()

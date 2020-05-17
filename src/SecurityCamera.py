from MotionDetector import MotionDetector
from camera.RaspberryCamera import RaspberryCamera
from runner.TimeRunner import TimeRunner

if __name__ == '__main__':
    cam = RaspberryCamera()
    runner = TimeRunner(10)
    detector = MotionDetector(cam, None, runner)
    detector.run()

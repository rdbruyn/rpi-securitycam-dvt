from MotionDetector import MotionDetector
from camera.RaspberryCamera import RaspberryCamera
from runner.TimeRunner import TimeRunner
from database.S3database import S3database
from time import sleep

if __name__ == '__main__':
    cam = RaspberryCamera()
    sleep(1)
    runner = TimeRunner(10)
    s3db = S3database()
    detector = MotionDetector(cam, s3db, runner)
    detector.run()

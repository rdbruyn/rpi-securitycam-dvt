from MotionDetector import MotionDetector
from camera.RaspberryCamera import RaspberryCamera
from runner.TimeRunner import TimeRunner
from database.S3database import S3database
from time import sleep
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t',
        '--time',
        type=int,
        help='Puts security camera on timed mode. Will run for this time before shutting down.',
        default=60
    )

    args = parser.parse_args()

    cam = RaspberryCamera()
    sleep(1)
    runner = TimeRunner(args.time)
    s3db = S3database()
    detector = MotionDetector(cam, s3db, runner)
    detector.run()

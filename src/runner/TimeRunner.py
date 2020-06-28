from .Runner import Runner
import time


class TimeRunner(Runner):

    def __init__(self, duration):
        self.start_time = time.time()
        self.duration = duration
        self.started = False

    def start(self):
        self.started = True

    def should_run(self):
        if self.started:
            current_time = time.time()
            return current_time - self.start_time < self.duration

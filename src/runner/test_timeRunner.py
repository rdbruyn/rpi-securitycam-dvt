from .TimeRunner import TimeRunner
import time


def test_givenRunnerRunsForLessThanDuration_whenCallingShouldRun_thenReturnTrue():
    time_runner = TimeRunner(.2)
    time_runner.start()
    time.sleep(.02)
    assert time_runner.should_run()


def test_givenRunnerRunsForMoreThanDuration_whenCallingShouldRun_thenReturnFalse():
    time_runner = TimeRunner(.1)
    time_runner.start()
    time.sleep(.15)
    assert not time_runner.should_run()

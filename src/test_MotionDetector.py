import numpy as np

from MotionDetector import MotionDetector


def test_givenTwoImagesThatDifferWithLessThanRatio_whenTestingForMovement_thenReturnFalse():
    ratio = .5
    threshold = 15
    input_image1 = np.asarray([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    input_image2 = np.asarray([[1, 1, 1], [1, 1, 1], [20, 20, 20]])
    detector = MotionDetector(None, None, None, ratio, .03, threshold)
    assert not detector.test_for_motion(input_image1, input_image2, ratio)


def test_givenTwoImagesThatDifferWithMoreThanRatio_whenTestingForMovement_thenReturnTrue():
    ratio = .5
    threshold = 15
    input_image1 = np.asarray([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    input_image2 = np.asarray([[1, 1, 1], [20, 20, 30], [20, 20, 20]])
    detector = MotionDetector(None, None, None, ratio, .03, threshold)
    assert detector.test_for_motion(input_image1, input_image2, .5)


# def test_whenStopSignalIsGiven_thenMotionDetectorStopsRunning():
#     mock_runner = Mock(spec=Runner)
#     mock_runner.should_run = Mock(return_value=True)
#     detector = MotionDetector(camera=None, database=None, runner=mock_runner)
#     detector.run()
#     detector.stop()
#     assert not detector.is_running

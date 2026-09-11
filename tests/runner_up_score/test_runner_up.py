from src.runner_up.util import find_runner_up


def test_runner_up():
    scores = [2, 3, 6, 6, 5]

    result = find_runner_up(scores)

    assert result == 5
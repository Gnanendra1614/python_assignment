from src.numpy_min_max.util import min_max


def test_min_max():
    numbers = [[3, 5, 1], [7, 2, 9], [4, 6, 8]]

    assert min_max(numbers) == 4
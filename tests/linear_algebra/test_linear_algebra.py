from src.linear_algebra.util import linear_algebra


def test_linear_algebra():
    matrix = [
        [1.1, 1.1],
        [1.1, 1.1]
    ]

    assert linear_algebra(matrix) == 0.0


def test_linear_algebra_second():
    matrix = [
        [2, 3],
        [4, 5]
    ]

    assert linear_algebra(matrix) == -2.0
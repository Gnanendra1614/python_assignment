from src.no_idea.util import calculate_happiness


def test_calculate_happiness():
    arr = [1, 5, 3, 3]
    A = {1, 3}
    B = {5, 7}

    assert calculate_happiness(arr, A, B) == 2
from src.iterables_and_iterators.util import find_probability


def test_find_probability():
    letters = ["a", "a", "c", "d"]
    k = 2

    result = find_probability(letters, k)

    assert result == 0.8333333333333334
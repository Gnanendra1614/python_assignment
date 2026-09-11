from src.mutations.util import mutate_string


def test_mutate_string():
    string = "abracadabra"

    result = mutate_string(string, 5, "k")

    assert result == "abrackdabra"


def test_mutate_string_first_position():
    string = "hello"

    result = mutate_string(string, 0, "H")

    assert result == "Hello"


def test_mutate_string_last_position():
    string = "hello"

    result = mutate_string(string, 4, "O")

    assert result == "hellO"
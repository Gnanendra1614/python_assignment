from src.calendar.util import find_day


def test_find_day():
    result = find_day(8, 5, 2015)

    assert result == "WEDNESDAY"


def test_find_day_monday():
    result = find_day(8, 3, 2020)

    assert result == "MONDAY"


def test_find_day_sunday():
    result = find_day(8, 2, 2020)

    assert result == "SUNDAY"
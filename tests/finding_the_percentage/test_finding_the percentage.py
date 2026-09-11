from src.find_percentage.util import find_percentage


def test_find_percentage():
    student_marks = {
        "Krishna": [67.0, 68.0, 69.0],
        "Arjun": [70.0, 98.0, 63.0],
        "Malika": [52.0, 56.0, 60.0]
    }

    result = find_percentage(student_marks, "Arjun")

    assert result == 77.0


def test_find_percentage_decimal():
    student_marks = {
        "Harry": [37.0, 40.0, 45.0],
        "Berry": [45.0, 40.0, 30.0],
        "Tina": [40.0, 50.0, 60.0]
    }

    result = find_percentage(student_marks, "Tina")

    assert result == 50.0
from src.print_formatting.util import print_formatted


def test_print_formatted(capsys):
    print_formatted(3)

    captured = capsys.readouterr()

    assert captured.out == (
        " 1  1  1  1\n"
        " 2  2  2 10\n"
        " 3  3  3 11\n"
    )


def test_print_formatted_five(capsys):
    print_formatted(5)
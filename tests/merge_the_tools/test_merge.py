from src.merge_the_tools.util import merge_the_tools


def test_merge_the_tools(capsys):
    string = "AABCAAADA"
    k = 3

    merge_the_tools(string, k)

    captured = capsys.readouterr()

    assert captured.out == "AB\nCA\nAD\n"


def test_merge_the_tools_with_unique_characters(capsys):
    string = "ABCDE"
    k = 2

    merge_the_tools(string, k)

    captured = capsys.readouterr()

    assert captured.out == "AB\nCD\nE\n"
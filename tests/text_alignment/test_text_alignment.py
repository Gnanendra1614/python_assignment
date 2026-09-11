from src.text_alignment.util import text_alignment


def test_text_alignment(capsys):
    text_alignment(1)

    captured = capsys.readouterr()

    expected = (
        "H\n"
        "H H\n"
        "HHHHH\n"
        "H H\n"
        "     H\n"
    )

    assert captured.out == expected
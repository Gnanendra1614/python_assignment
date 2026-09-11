from src.piling_up.util import piling_up


def test_piling_up():
    blocks = [4, 3, 2, 1, 3, 4]

    assert piling_up(blocks) == "Yes"


def test_piling_up_no():
    blocks = [4, 3, 2, 1, 3, 4, 5]

    assert piling_up(blocks) == "No"
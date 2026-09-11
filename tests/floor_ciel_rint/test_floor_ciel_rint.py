from src.floor_ciel_rint.util import floor_ceil_rint


def test_floor_ceil_rint():
    values = [1.1, 2.5, 3.7]

    floor_result, ceil_result, rint_result = floor_ceil_rint(values)

    assert floor_result.tolist() == [1.0, 2.0, 3.0]
    assert ceil_result.tolist() == [2.0, 3.0, 4.0]
    assert rint_result.tolist() == [1.0, 2.0, 4.0]
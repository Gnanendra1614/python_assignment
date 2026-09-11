from src.time_delta.util import time_delta


def test_time_delta():
    t1 = "Sun 10 May 2015 13:54:36 -0700"
    t2 = "Sun 10 May 2015 13:54:36 -0000"

    result = time_delta(t1, t2)

    assert result == "25200"

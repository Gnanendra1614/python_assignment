from src.numpy_mean_var_std.util import mean_var_std


def test_mean_var_std():
    numbers = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    mean_result, var_result, std_result = mean_var_std(numbers)

    assert mean_result.tolist() == [2.0, 5.0]
    assert var_result.tolist() == [2.25, 2.25, 2.25]
    assert std_result == 1.70782512766
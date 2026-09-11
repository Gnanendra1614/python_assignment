from src.lists.util import command_op


def test_append():
    my_list = []

    command_op(my_list, ["append", "10"])

    assert my_list == [10]


def test_insert():
    my_list = [10]

    command_op(my_list, ["insert", "0", "5"])

    assert my_list == [5, 10]


def test_remove():
    my_list = [10, 20, 30]

    command_op(my_list, ["remove", "20"])

    assert my_list == [10, 30]


def test_sort():
    my_list = [30, 10, 20]

    command_op(my_list, ["sort"])

    assert my_list == [10, 20, 30]


def test_pop():
    my_list = [10, 20, 30]

    command_op(my_list, ["pop"])

    assert my_list == [10, 20]


def test_reverse():
    my_list = [10, 20, 30]

    command_op(my_list, ["reverse"])

    assert my_list == [30, 20, 10]
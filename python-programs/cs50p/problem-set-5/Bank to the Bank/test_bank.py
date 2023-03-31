from bank import value


def test_value_1():
    assert value("Hello") == "$0"


def test_value_2():
    assert value("What's up!") == "$100"

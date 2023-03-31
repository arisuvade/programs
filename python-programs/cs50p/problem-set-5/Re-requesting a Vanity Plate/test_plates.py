from plates import is_valid


def main():
    test_valid_1()
    test_valid_2()
    test_valid_3()
    test_valid_4()


def test_valid_1():
    assert is_valid("HELLO, WORLD123") is False


def test_valid_2():
    assert is_valid("HAHAHAHAHAHAHA111111") is False


def test_valid_3():
    assert is_valid("111111") is False


def test_valid_4():
    assert is_valid("CS50") is True

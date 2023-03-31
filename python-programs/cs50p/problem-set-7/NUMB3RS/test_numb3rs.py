from numb3rs import validate


def main():
    test_validate1()
    test_validate2()


def test_validate1():
    assert validate("1.1.1.1") == True
    assert validate("11.11.11.11") == True
    assert validate("111.111.111.111") == True


def test_validate2():
    assert validate("256.111.111.111") == False
    assert validate("1111.1111.1111") == False
    assert validate("cat") == False


if __name__ == "__main__":
    main()

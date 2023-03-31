from working import convert


def main():
    test_convert_1()
    test_convert_2()
    test_convert_3()
    test_convert_4()


def test_convert_1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_convert_2():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_convert_3():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"


def test_convert_4():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


if __name__ == "__main__":
    main()

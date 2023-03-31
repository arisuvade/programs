from seasons import get_minutes, get_date


def main():
    test_get_date()
    test_get_minutes()


def test_get_date():
    assert get_date("2004-3-1") == (2004, 3, 1)


def test_get_minutes():
    assert get_minutes(
        2004, 3, 1) == "Nine million, seven hundred and sixty-three thousand, two hundred minutes"


if __name__ == "__main__":
    main()

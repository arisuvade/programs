from jar import Jar

jar = Jar()


def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()


def test_init():
    global jar
    assert str(jar) == ""


def test_str():
    global jar
    assert str(jar) == ""


def test_deposit():
    global jar
    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_withdraw():
    global jar
    jar.withdraw(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"


if __name__ == "__main__":
    main()

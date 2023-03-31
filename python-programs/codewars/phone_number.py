# def create_phone_number(n: str) -> str:
#     a, b, c = n[0:3], n[3:6], n[6:10]
#     d = "".join([str(i) for i in a])
#     e = "".join([str(i) for i in b])
#     f = "".join([str(i) for i in c])
#     return f"({d}) {e}-{f}"


def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


def main() -> None:
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


if __name__ == "__main__":
    main()

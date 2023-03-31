grocery = {}


def main():
    grocery_list()


def grocery_list():
    while True:
        try:
            item = input()
        except KeyboardInterrupt:
            print()
            break
        if item.upper() in grocery:
            grocery[item.upper()] += 1
        else:
            grocery[item.upper()] = 1

    for item in sorted(grocery.keys()):
        print(grocery[item], item)


if __name__ == "__main__":
    main()

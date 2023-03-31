import sys
import csv
import tabulate


def main():
    pizza = arg_validator()
    menu = menu_validator(pizza)
    print(menu)


def arg_validator():
    if len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):
        return sys.argv[1]
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


def menu_validator(m):
    try:
        with open(m) as file:
            reader = csv.DictReader(file)
            return (tabulate.tabulate
                        (reader, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()

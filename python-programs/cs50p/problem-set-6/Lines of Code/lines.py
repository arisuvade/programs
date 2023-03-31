import sys


def main():
    file_checker()
    file = length_checker()
    lines = line_counter(file)
    print(lines)


def file_checker():
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")


def length_checker():
    if len(sys.argv) == 2:
        return sys.argv[1]
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


def line_counter(f):
    try:
        with open(sys.argv[1]) as file:
            line_count = 0
            for line in file:
                line = line.lstrip()
                if (not line.startswith("#")
                        and line != ""):
                    line_count += 1
            return line_count
    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()

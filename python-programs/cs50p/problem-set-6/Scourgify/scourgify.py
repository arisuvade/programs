import sys
import csv


def main():
    before, after = arg_counter()
    read_write(before, after)


def arg_counter():
    if len(sys.argv) == 3:
        return sys.argv[1], sys.argv[2]
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


def read_write(before, after):
    try:
        with open(before) as file1:
            reader = csv.DictReader(file1)
            with open(after, "w") as file2:
                writer = csv.DictWriter(
                    file2, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                    row["first"] = row.pop("name")
                    last_name, first_name = row["first"].split(", ")
                    row["first"] = first_name
                    row["last"] = last_name
                    writer.writerow(row)
    except FileNotFoundError:
        sys.exit(f"Could not read {before}")


if __name__ == "__main__":
    main()

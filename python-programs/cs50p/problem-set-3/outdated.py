months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        try:
            user_input = input("Date: ").capitalize()
            if "/" in user_input:
                date = slash(user_input)
                if date:
                    print(date)
                else:
                    continue
                break
            elif "," in user_input:
                user_input = user_input.replace(",", "")
                date = space_comma(user_input)
                if date:
                    print(date)
                else:
                    continue
                break
        except ValueError:
            continue


def slash(d):
    month, day, year = d.split("/")
    try:
        if int(month) > 12 or int(day) > 31:
            return False
        else:
            return f"{year}-{int(month):02}-{int(day):02}"
    except ValueError:
        return False


def space_comma(d):
    month, day, year = d.split(" ")
    if month in months:
        month = months.index(month) + 1
        if int(day) <= 31:
            return f"{year}-{int(month):02}-{int(day):02}"
        else:
            return False


if __name__ == "__main__":
    main()

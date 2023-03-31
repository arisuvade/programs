def main():
    dollars = dollars_to_float(
        input("How much was the meal? "))
    percent = percent_to_float(
        input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    cost = float(d.replace("$", ""))
    return cost


def percent_to_float(p):
    tip_percent = float(p.replace("%", "")) / 100
    return tip_percent


main()

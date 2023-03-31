def main():
    fraction = input("Fraction: ")
    convertion = convert(fraction)
    percent = gauge(convertion)
    print(percent)


def convert(fraction):
    while True:
        if len(fraction) != 3 or fraction[1] != "/":
            fraction = input("Fraction: ")
            continue
        else:
            pass

        try:
            if fraction[0].isdigit() and fraction[2].isdigit():
                pass
            else:
                fraction = input("Fraction: ")
                continue
        except ValueError:
            continue

        numerator, denominator = fraction.split("/")
        x = int(numerator)
        y = int(denominator)

        try:
            quotient = x / y
            result = quotient * 100
        except ZeroDivisionError:
            fraction = input("Fraction: ")
            continue

        if x > y:
            fraction = input("Fraction: ")
            continue
        else:
            pass

        return result


def gauge(percentage):
    if percentage > 99:
        return "F"
    elif percentage <= 0:
        return "E"
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()

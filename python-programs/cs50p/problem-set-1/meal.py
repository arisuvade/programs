def main():
    input_time = input("What time is it? ")
    hours, minutes = input_time.split(":")
    result = convert(int(hours), int(minutes))
    should_return = result
    match result:
        case "It's breakfast time." | "It's lunch time." | "It's dinner time.":
            print(result)
        case _:
            print(should_return)


def convert(hours, minutes):
    if hours >= 7 and hours <= 8:
        return "It's breakfast time."
    elif hours >= 12 and hours <= 13:
        return "It's lunch time."
    elif hours >= 18 and hours <= 19:
        return "It's dinner time."
    else:
        minute = 60 - minutes
        if hours >= 1 and hours <= 6:
            if hours == 1:
                return f"Return in 5 hours and {minute} minute(s)."
            elif hours == 2:
                return f"Return in 4 hours and {minute} minute(s)."
            elif hours == 3:
                return f"Return in 3 hours and {minute} minute(s)."
            elif hours == 4:
                return f"Return in 2 hours and {minute} minute(s)."
            elif hours == 5:
                return f"Return in 1 hours and {minute} minute(s)."
            elif hours == 6:
                return f"Return in {minute} minute(s)."
        elif hours >= 13 and hours <= 17:
            if hours == 13:
                return f"Return in 4 hours and {minute} minute(s)."
            elif hours == 14:
                return f"Return in 3 hours and {minute} minute(s)."
            elif hours == 15:
                return f"Return in 2 hours and {minute} minute(s)."
            elif hours == 16:
                return f"Return in 1 hours and {minute} minute(s)."
            elif hours == 17:
                return f"Return in {minute} minute(s)."
        elif hours >= 20 and hours <= 24:
            if hours == 20:
                return f"Return in 11 hours and {minute} minute(s)."
            elif hours == 21:
                return f"Return in 10 hours and {minute} minute(s)."
            elif hours == 22:
                return f"Return in 9 hours and {minute} minute(s)."
            elif hours == 23:
                return f"Return in 8 hours and {minute} minute(s)."
            elif hours == 24:
                return f"Return in 7 hours and {minute} minute(s)."


if __name__ == "__main__":
    main()

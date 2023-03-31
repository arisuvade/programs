def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0:1].isalpha() is False:
        return False
    if s[-1].isdigit() is False:
        return False

    i = 0
    while i < len(s):
        if s[i].isalpha() is False:
            if s[i] == "0":
                return False
            else:
                break
        i += 1

    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

    if s.isalnum():
        return True
    else:
        return False


main()

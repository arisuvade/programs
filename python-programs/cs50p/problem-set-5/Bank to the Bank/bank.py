def main():
    greeting = input("Greeting: ").capitalize()
    result = value(greeting)
    print(result)


def value(greeting):
    forbidden_greeting = "Hello"
    forbidden_letter = "H"
    if greeting == forbidden_greeting:
        return "$100"
    elif (forbidden_letter in greeting[0] and
          forbidden_greeting not in greeting):
        return "$20"
    elif greeting >= forbidden_greeting:
        return "$0"
    else:
        return "$0"


if __name__ == "__main__":
    main()

vowels = ["a", "e", "i", "o", "u"]


def main():
    while True:
        try:
            word = input("Input: ")
            break
        except ValueError:
            continue
    result = shorten(word)
    print(f"Output: {result}")


def shorten(word):
    result = ""
    for letter in word:
        if letter not in vowels:
            result += letter
    return result


if __name__ == "__main__":
    main()

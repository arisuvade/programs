import random


def main():
    level = levels()
    while True:
        guess = guesses()
        if guess < level:
            print("Too small!")
        elif guess > level:
            print("Too large!")
        else:
            print("Just right")
            break


def levels():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
            else:
                continue
        except ValueError:
            continue
    answer = random.randint(1, level)
    return answer


def guesses():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                break
            else:
                continue
        except ValueError:
            continue
    return guess


if __name__ == "__main__":
    main()

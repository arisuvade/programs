import random


def main():
    level = get_level()
    questions = generate_integer(level)
    print(questions)


def get_level():
    while True:
        level = int(input("Level: "))
        if level >= 1 and level <= 3:
            return level
        else:
            raise ValueError


def generate_integer(level):
    score = 0
    trial = 0
    for _ in range(10):
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        else:
            x = random.randint(100, 999)
            y = random.randint(100, 999)

        while True:
            print(f"{x} + {y} = ", end="")
            answer = input()
            if answer == str(x + y):
                score += 1
                break
            elif answer != str(x + y) and trial != 3:
                trial += 1
                print("EEE")
                continue
            else:
                print("EEE")
                print(f"{x} + {y} = {x + y}")
                break
    print(f"Score: {score}")


if __name__ == "__main__":
    main()

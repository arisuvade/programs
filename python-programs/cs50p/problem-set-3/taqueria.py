menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    food_cost()


def food_cost():
    total = 0
    while True:
        try:
            item = input("Item: ").title()
        except KeyboardInterrupt:
            print()
            break
        if item in menu:
            total += menu[item]
            print(f"Total: ${total}")


if __name__ == "__main__":
    main()

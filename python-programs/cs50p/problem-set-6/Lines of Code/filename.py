print("Hello, world!")

# this
# is
# only
# a
# test
# file

# Stores a name in a variable

name = input("What's your name? ")
print(f"hello, {name}")

# Unpacks a list

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

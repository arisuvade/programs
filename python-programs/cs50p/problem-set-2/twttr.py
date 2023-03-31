vowels = ["a", "e", "i", "o", "u"]
input = input("Input: ")
output = ""

for letter in input:
    if letter not in vowels:
        output += letter

print(f"Output: {output}")

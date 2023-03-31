expression = input("Expression: ")
x, y, z = expression.split(" ")

a = float(x)
b = float(z)

if y == "+":
    result = a + b
    print(result)
elif y == "-":
    result = a - b
    print(result)
elif y == "*":
    result = a * b
    print(result)
elif y == "/":
    result = a / b
    print(result)

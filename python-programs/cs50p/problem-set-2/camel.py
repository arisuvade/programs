camel_case = input("camelCase: ")
camel_case = camel_case[0].lower() + camel_case[1:]

for i in camel_case:
    if i.isupper():
        snake_case = camel_case.replace(i, f"_{i.lower()}")

print(f"snake_case: {snake_case}")

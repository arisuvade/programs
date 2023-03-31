# def camel_case(string: str) -> str:
#     words: list[str] = string.split(" ")
#     return "".join(i.capitalize() for i in words)


def camel_case(string):
    return string.title().replace(" ", "")


print(camel_case("test case"))
print(camel_case("camel case method"))
print(camel_case("say hello "))
print(camel_case(" camel case word"))
print(camel_case(""))

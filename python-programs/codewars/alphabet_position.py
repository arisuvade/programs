# from string import ascii_letters, ascii_lowercase


# def alphabet_position(text: str):
#     letters: list[str] = [i.lower() for i in text if i in ascii_letters]
#     order: list[str] = [str(ascii_lowercase.index(i) + 1) for i in letters]
#     return " ".join(order)


def alphabet_position(text):
    return " ".join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("The narwhal bacons at midnight."))

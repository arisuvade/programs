def first_non_repeating_letter(string: str) -> str:
    for i in string:
        if string.lower().count(i.lower()) == 1:
            return i
    return ""


print(first_non_repeating_letter("a"))
print(first_non_repeating_letter("stress"))
print(first_non_repeating_letter("moonmen"))
print(first_non_repeating_letter(""))
print(first_non_repeating_letter("sTreSS"))

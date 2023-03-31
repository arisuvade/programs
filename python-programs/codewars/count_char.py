# def count(string: str) -> dict:
#     letter_dict = {}
#     individual_letter = [i for i in set(string)]
#     count = []
#     c = 0
#     for i in individual_letter:
#         count.append(string.count(i))
#         letter_dict[i] = count[c]
#         c += 1
#     return letter_dict


def count(string):
    return {i: string.count(i) for i in string}


print(count("aba"))
print(count(""))

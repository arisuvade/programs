def odd_or_even(arr: list[int]):
    return "odd" if sum(arr) % 2 else "even"


print(odd_or_even([0, 1, 2]))
print(odd_or_even([0, 1, 3]))
print(odd_or_even([1023, 1, 2]))

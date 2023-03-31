def move_zeros(lst: list[int]) -> list[int]:
    nums = [int(x) for x in lst if x != 0]
    zero = [int(x) for x in lst if x == 0]
    return nums + zero


print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))

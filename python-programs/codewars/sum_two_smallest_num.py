def sum_two_smallest_numbers(numbers: list[int]) -> int:
    numbers.sort()
    return numbers[0] + numbers[1]

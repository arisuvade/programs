"""Challenge: Fibonacci Sequence
Write a Python function called fibonacci that takes an integer n as input and returns a list of the first n numbers in the Fibonacci sequence. The Fibonacci sequence is a series of numbers in which each number (after the first two) is the sum of the two preceding ones. The sequence starts with 0 and 1.

For example:

fibonacci(0) should return an empty list []
fibonacci(1) should return [0]
fibonacci(5) should return [0, 1, 1, 2, 3]
fibonacci(10) should return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]"""


def fibonacci(set: int) -> list[int]:
    first_term: int = 0
    second_term: int = 1
    third_term: int = 0

    fibonacci_list: list[int] = []

    for _ in range(set):
        fibonacci_list.append(first_term)
        first_term = second_term + third_term
        second_term = third_term
        third_term = first_term

    return fibonacci_list


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(5))
print(fibonacci(10))

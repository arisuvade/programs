"""Challenge: Unique Elements Counter
Write a Python function called count_unique_elements that takes a list as input and returns the count of unique elements in that list. The count should not include any duplicates.

For example:

count_unique_elements([1, 2, 3, 4, 5]) should return 5
count_unique_elements([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) should return 5
count_unique_elements(['a', 'b', 'c', 'a', 'b', 'c']) should return 3
"""


def count_unique_elements(elements: list[int | str]) -> int:
    unique_elements: list[int | str] = []

    for element in elements:
        if element not in unique_elements:
            unique_elements.append(element)

    return len(unique_elements)


print(count_unique_elements([1, 2, 3, 4, 5]))
print(count_unique_elements([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))
print(count_unique_elements(["a", "b", "c", "a", "b", "c"]))

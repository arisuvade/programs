def invert(lst: list[int]) -> list[int]:
    return [abs(x) if x != abs(x) else -abs(x) for x in lst]

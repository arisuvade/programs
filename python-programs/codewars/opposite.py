def opposite(number: int | float) -> int | float:
    if number != 0:
        return abs(number) if number < 0 else -abs(number)
    return number

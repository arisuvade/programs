def descending_order(num: int) -> int:
    return int("".join(sorted([x for x in str(num)], reverse=True)))

def count_sheeps(sheep: list[bool]) -> int:
    return len([t for t in sheep if t is True])

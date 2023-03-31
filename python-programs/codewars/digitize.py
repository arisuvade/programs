def digitize(n: int) -> list[int]:
    return [int(x) for x in str(n)][::-1]

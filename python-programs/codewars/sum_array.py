def sum_array(arr: list[int] | None) -> int:
    if arr is None or len(arr) in range(0, 3):
        return 0
    return sum([x for x in sorted(arr)][1:-1])

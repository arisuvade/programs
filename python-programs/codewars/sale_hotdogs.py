def sale_hotdogs(n: int) -> int:
    return n * 100 if (n < 5) else n * 95 if (n < 10) else n * 90

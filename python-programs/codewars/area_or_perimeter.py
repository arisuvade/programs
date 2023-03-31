def area_or_perimeter(l: int, w: int) -> int:
    return l * w if l == w else (l + l) + (w + w)

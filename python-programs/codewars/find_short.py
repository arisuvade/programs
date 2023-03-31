def find_short(s: str) -> int:
    return len(min(s.split(), key=len))

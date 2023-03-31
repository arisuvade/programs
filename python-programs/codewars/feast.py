def feast(beast: str, dish: str) -> bool:
    return True if beast[0] == dish[0] and beast[-1] == dish[-1] else False

def get_count(sentence: str) -> int:
    return len([v for v in sentence if v in "aeiou"])

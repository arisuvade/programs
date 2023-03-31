def to_jaden_case(string: str) -> str:
    return " ".join([w.capitalize() for w in string.split()])

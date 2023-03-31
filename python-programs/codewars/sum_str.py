def sum_str(a: str, b: str) -> str:
    if a == "" and b == "":
        return "0"
    elif a == "":
        return b
    elif b == "":
        return a
    else:
        return f"{int(a) + int(b)}"

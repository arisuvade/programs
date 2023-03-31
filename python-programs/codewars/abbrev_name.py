def abbrev_name(name: str) -> str:
    return ".".join([i[0] for i in name.upper().split()])

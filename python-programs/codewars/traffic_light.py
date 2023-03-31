def update_light(current: str) -> str:
    match current:
        case "green":
            return "yellow"
        case "yellow":
            return "red"
        case _:
            return "green"

def validate_pin(pin: str) -> bool:
    if pin.isnumeric():
        if len(pin) in (4, 6):
            return True
    return False

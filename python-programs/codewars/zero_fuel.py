def zero_fuel(distance_to_pump: int, mpg: int, fuel_left: int) -> bool:
    return True if distance_to_pump - (mpg * fuel_left) < 5 else False

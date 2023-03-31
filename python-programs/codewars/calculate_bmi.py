def bmi(weight: int | float, height: int | float) -> str:
    result = weight / (height**2)
    if result <= 18.5:
        return "Underweight"
    elif result <= 25:
        return "Normal"
    elif result <= 30:
        return "Overweight"
    return "Obese"

from statistics import mean as average


def better_than_average(class_points: list[int], your_points: int) -> bool:
    return True if your_points > average(class_points) else False

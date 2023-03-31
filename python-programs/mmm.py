from sys import argv
from statistics import mean, median, mode


numbers = [float(n) for n in argv[1:]]

print(f"Mean:   {mean(numbers)}")
print(f"Median: {median(numbers)}")
print(f"Mode:   {mode(numbers)}")

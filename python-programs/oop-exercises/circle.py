from dataclasses import dataclass
from math import pi


@dataclass
class Circle:
    a: int
    b: int
    r: int

    def area(self) -> int:
        return round(pi * self.r**2)

    def perimeter(self) -> int:
        return round(2 * pi * self.r)

    def form_equation(self, x: int, y: int) -> int:
        return (x - self.a) ** 2 + (y - self.b) ** 2 - self.r**2

    def test_belong(self, x: int, y: int):
        if self.form_equation(x, y) == 0:
            print(f"Point: {x}, {y}) belong")
        else:
            print(f"Point: ({x}, {y}) does not belong")


c1 = Circle(5, 5, 5)
print(f"Area: {c1.area()}")
print(f"Perimeter: {c1.perimeter()}")
c1.test_belong(5, 5)

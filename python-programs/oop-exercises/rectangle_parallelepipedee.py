from dataclasses import dataclass


@dataclass
class Rectangle:
    length: int
    width: int

    def perimeter(self) -> int:
        return 2 * (self.length + self.width)

    def area(self) -> int:
        return self.length * self.width

    def display(self):
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Perimeter: {self.perimeter()}")
        print(f"Area: {self.area()}")


r1 = Rectangle(7, 5)
r1.display()


@dataclass
class Parallelepipede(Rectangle):
    height: int

    def volume(self):
        print(f"Volume: {self.area() * self.height}")


p1 = Parallelepipede(7, 5, 2)
p1.volume()

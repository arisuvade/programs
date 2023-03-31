from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


p1 = Person("Pedro", 29)
p1.display()


@dataclass
class Student(Person):
    section: str

    def display(self):
        super().display()
        print(f"Student: {self.section}")


s1 = Student("Juan", 12, "B")
s1.display()

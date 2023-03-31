from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    price: int

    def view(self):
        print(f"Book Title: {self.title}")
        print(f"Book Author: {self.author}")
        print(f"Book Price: ₱{self.price:,}")


b1 = Book("Harry Potter", "J.K. Rowling", 10_000)
b1.view()

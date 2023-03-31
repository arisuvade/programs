from dataclasses import dataclass


@dataclass
class Computation:
    @staticmethod
    def factorial(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * Computation.factorial(n - 1)

    @staticmethod
    def sum(*n: int) -> int:
        return sum(n)

    @staticmethod
    def test_prim(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def test_prims(x: int, y: int):
        common_div: int = 0
        for i in range(1, x + 1):
            if x % i == 0 and y % i == 0:
                common_div += 1
        if common_div == 1:
            print("The numbers", x, "and", y, "are co-primes")
        else:
            print("The numbers", x, "and", y, "are not co-primes")

    @staticmethod
    def table_mult(x: int):
        for n in range(1, 10):
            print(n, "x", x, "=", n * x)

    @staticmethod
    def all_tables_mult():
        for k in range(1, 10):
            print("Multiplication table:", k, "is:")
            for i in range(1, 10):
                print(i, "x", k, "=", i * k)

    @staticmethod
    def list_div(n: int) -> list[int]:
        l_div: list[int] = []
        for i in range(1, n + 1):
            if n % i == 0:
                l_div.append(i)
        return l_div

    @staticmethod
    def list_div_prim(n: int) -> list[int]:
        l_div: list[int] = []
        for i in range(1, n + 1):
            if n % i == 0 and Computation.test_prim(i):
                l_div.append(i)
        return l_div


print(Computation.factorial(5))
print(Computation.sum(5, 5, 5, 5, 5))
print(Computation.test_prim(5))
Computation.test_prims(5, 10)
Computation.table_mult(5)
Computation.all_tables_mult()
print(Computation.list_div(5))
print(Computation.list_div_prim(5))

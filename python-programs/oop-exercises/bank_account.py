from dataclasses import dataclass


@dataclass
class BankAccount:
    account_number: int
    name: str
    balance: int

    BANK_FEE: float = 0.05  # 5%

    def deposit(self, deposit_amount: int):
        self.balance += deposit_amount

    def withdrawal(self, withdrawal_amount: int):
        if self.balance >= withdrawal_amount:
            self.balance -= withdrawal_amount

    def bank_fees(self):
        self.balance -= int(self.balance * self.BANK_FEE)

    def display(self):
        print(f"Account No.: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Balance: ₱{self.balance:,}")


ba1 = BankAccount(1234, "John Cena", 10_000)
ba1.display()

deposit_amount: int = 4_000
ba1.deposit(deposit_amount)
print(f"After deposited: ₱{ba1.balance:,}")

withdrawal_amount: int = 7_000
ba1.withdrawal(withdrawal_amount)
print(f"After withdrawal: ₱{ba1.balance:,}")

ba1.bank_fees()
print(f"After bank fees: ₱{ba1.balance:,}")

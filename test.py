from bank import *

Vishal = BankAccount(1000, "Vishal")
Prajkata = BankAccount(2000, "Prajkata")

Vishal.deposit(1000)

Vishal.transfer(100, Prajkata)
Vishal.get_balance()

print("......................................................................")

shirish = InterestAccount(1000, "Shirish")
shirish.get_balance()
shirish.deposit(1000)
shirish.transfer(1100, Vishal)

print("......................................................................")

guru = SavingsAccount(1000, "Guru")

guru.withdraw(100)
guru.get_balance()

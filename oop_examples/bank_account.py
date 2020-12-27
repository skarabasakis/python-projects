import random
from string import digits

class BankAccount:
    def __init__(self):
        self.number = ''.join(random.choices(digits, k=12))
        self.balance = 0

    def withdraw(self, amount):
        assert amount <= self.balance
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

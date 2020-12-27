import random
from string import digits

class BankAccount:
    def __init__(self):
        self.number = ''.join(random.choices(digits, k=12))
        self.balance = 0

    def

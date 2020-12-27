class Teacher:
    def __init__(self, name, bank_account):
        self.name = name
        self.bank_account = bank_account

class FullTimeTeacher(Teacher):
    def __init__(self, name, bank_account, salary):
        super().__init__(name, bank_account)
        self.salary = salary

    def pay(self):
        self.bank_account.deposit(self.salary)

class HourlyPaidTeacher(Teacher):
    def __init__(self, name, bank_account, rate):
        super().__init__(name, bank_account)
        self.rate = rate

    def pay(self, hours):
        self.bank_account.deposit(self.rate * hours)

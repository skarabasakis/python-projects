class Teacher:
    def __init__(self, name, grade, salary):
        self.name = name
        self.grade = grade
        self.salary = salary

    def promote(self):
        self.grade += 1
        return self.grade

    def pay(self, bank_account):
        bank_account.deposit(self.salary)

class HourlyPaidTeacher(Teacher):
    def pay(self, bank_account, hours):
        bank_account.deposit(self.salary * hours)

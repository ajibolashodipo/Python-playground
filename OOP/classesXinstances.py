class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

emp_1 = Employee("Ajibola", "Shodipo", 300)
emp_2 = Employee("Tobi", "Ajibola", 456)

# print(emp_1.email)
# print(emp_1.fullname())
# print(Employee.fullname(emp_1))

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

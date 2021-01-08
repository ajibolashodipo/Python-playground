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
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None ):
        super().__init__(first,last, pay)
        if employees is None:
            self.employees= []
        else:
            self.employees= employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())


dev_1 = Developer("Ajibola", "Shodipo", 300, "Python")
emp_2 = Developer("Tobi", "Ajibola", 456, "Java")

# print(emp_1.email)
# print(emp_1.fullname())
# print(Employee.fullname(emp_1))

# print(emp_2.pay)
# emp_1.apply_raise()
# print(emp_1.prog_lang)
# print(help(Developer))

mgr_1= Manager ("Sue", "Smith", 90000, [dev_1])

print(mgr_1.email)
mgr_1.add_emp(emp_2)
mgr_1.print_emps()
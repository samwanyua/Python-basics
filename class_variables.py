'''
Class variables - variables shared among all instances of a class
'''
class Employee:

    raise_amount = 1.09
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employees += 1

    def fullname(self):
        return f"{self.first} {self.last} - {self.pay}"
    
    def appy_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
emp_1 = Employee('Kimani', 'Njoroge', 45000)
empy_2 = Employee('Angeiessfd', 'werjksjjf', 342314)
emp_3 = Employee('Henry','Mwangi', 32300)
print(emp_1.fullname())
print(Employee.fullname(empy_2))

print(emp_1.pay)
emp_1.appy_raise()
print(emp_1.pay)

print(Employee.__dict__)
print(emp_1.raise_amount)

emp_1.raise_amount = 1.06
print(emp_1.__dict__)

print(Employee.num_of_employees)


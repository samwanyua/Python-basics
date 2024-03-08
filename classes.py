# Oop in python
'''
Class is a blueprint for creating instances
An object is an instance of a class
'''
class Employee:
    def __init__(self,first_name, last_name, pay ): # constructor
        self.first_name = first_name # same as empy_1.first = 'Corey'
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@company.com'

    def fullName(self):
        return f"{self.first_name} {self.last_name}"

empy_1 = Employee('Cinery', 'Mustisya', 43000)
empy_2 = Employee('Tifanny', 'Mianai', 3423324)

print(empy_1.email)
print(empy_2.fullName())
print(Employee.fullName(empy_1))

'''#employee objects
empy_1 = Employee()
empy_2 = Employee()

print(empy_1)
print(empy_2)

# instance variables
empy_1.first = 'Corey'
empy_1.last = 'Schafer'
empy_1.email = 'corey@gmail.com'
empy_1.pay = 50000


empy_2.first = 'Collins'
empy_2.last = 'Muema'
empy_2.email = 'colomuema@gmail.com'
empy_2.pay = 70000

print(empy_2.email)
print(empy_1.email)

'''


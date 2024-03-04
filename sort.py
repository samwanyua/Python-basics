# sorting lists, sets, tuples, dicts, objects

my_list = [9,1,8,2,7,3,6,4,5]

s_list = sorted(my_list, reverse=True) #return new sorted list
print('Sorted list: \t',s_list)
print('Original list: ',my_list)

# sorting original list
my_list.sort(reverse=True)
print(my_list)

# sorting tuple
my_tuple = (9,1,8,2,7,3,6,4,5)
s_tup = sorted(my_tuple)
print(s_tup)

# sorting a dict
di = {'name':'Corey', 'job':'programming', 'age':'34', 'os': 'mac'}
s_di = sorted(di)
print(s_di) #sort keys

# sorting based on abs
li = [-6,-5,-4,1,2,3]
s_li = sorted(li)
print(s_li) #-6, -5, -4, 1, 2, 3]

s_li = sorted(li, key=abs)
print(s_li)


# sorting objects
class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f'{self.name}, {self.age}, ${self.salary}'
e1 = Employee('Carl',35,70000)
e2 = Employee('Sarah',24,30000)
e3 = Employee('John',45,84300)

employees = [e1,e2,e3]

# def e_sort(emp):
#     return emp.salary

# s_empoyees = sorted(employees, key=e_sort, reverse=True)
# print(s_empoyees)

# Using lambda function
s_empoyees = sorted(employees, key=lambda e: e.salary, reverse=True)
print(s_empoyees)
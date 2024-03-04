def greetings(greeting, name): 
   print(f"{greeting}, {name}")

# print(greetings().upper())
greetings("Jambo", "Nicodemous")


def student_info(*args, **kwargs):
   print(args) #('Math', 'Art')
   print(kwargs) #{'name': 'John', 'age': 22, 'email': 'Johnte@gmail.com'}
   
courses = ['Math', 'Art']
info = { 'name': 'John', 'age' : 22, 'email' : 'Johnte@gmail.com'}

student_info(*courses, **info)


# Practice
month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
   return year %4 == 0 and (year % 100 !=0 or year % 400 ==0)

print(is_leap(2004))

def days_in_month(year,month):
   if not 1 <= month <=12: # check if month is between 1 and 12
    return 'Invalid month'
   if month == 2 and is_leap(year):
    return 29;

    return month_days(month)
   
print(days_in_month(2016,2))

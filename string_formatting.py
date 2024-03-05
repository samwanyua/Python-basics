# formatting strings

person = {'name': 'Jenn', 'age': 23}
sentence = f"My name is {person['name']} and I am {person['age']} years old."
print(sentence)

calculation = f" 4 times 11 is equal to {4 * 11}"
print(calculation)

for n in range(1,11):
    sent = f"The value is {n:07}" # to add zero padding
    print(sent)

pi = 3.14159265
line = f"Pi is equal to {pi:.2f}"  #to 4 digits
print(line)

# printing dates
from datetime import datetime
birthday = datetime(1990,4,1)
line_b = f"Jenn has a birthday on {birthday:%B %d, %Y}" # Check python documentation
print(line_b)
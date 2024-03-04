# working with key value pairs
student = {
    'name': 'Kimani wa Njoroge',
    'age': 25,
    'courses': ['Front dev', 'Analyst']
}

print(student)
# print(student['name'])
print(student.get('name'))

# accessing a key that doesn't exist and a default value
print(student.get('phone', 'Not found')) 

# adding more elements
student['email'] = 'kimani@gmail.com'
print(student)

# updating a key
student['age'] = 324
print(student)

# using update method
student.update({'name': 'Jennifer', 'email': 'jeniffer27@gmail.com'})
print(student)

# deleting key
del student['courses']
print(student)

# using pop method
age = student.pop('age')
print(age)

# see no. of keys
print(len(student))

# to see all keys
print(student.keys())

# to see all values
print(student.values())

# to see all values and keys
print(student.items())

# looping keys
for key in student:
    print(key)

# looping keys and values
for key, value in student.items():
    print(key,value)

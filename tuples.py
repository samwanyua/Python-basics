# tuples are immutable
courses = ('History', 'Math', 'Physics','Chem', 'Bio', 'Bio')
print(courses)

for index, course in enumerate(courses):
    print(index, course)
    
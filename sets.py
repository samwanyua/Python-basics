# sets - unordered, unindexed, no duplicates
courses = {'History', 'Math', 'Physics','Chemistry', 'Bio-tech', 'Bio'} #duplicate values are gotten rid of
skills = {'History', 'Eng', 'Physics','Chem', 'Bio-chem', 'Bio-neuron'} 

print(courses)

# sets tests whether a value is part of the test
print('Math' in courses) 

# checking something sets have in common
print(courses.intersection(skills)) 

# checking the difference
print(courses.difference(skills)) 

# combining sets
print(courses.union(skills)) 

# creating empty lists, tuple and sets
empty_list = []

empty_tuple = ()

empty_set = set()

empty_dict = {}



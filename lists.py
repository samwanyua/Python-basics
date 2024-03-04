# lists - sequentials, indexed, ordered, allow duplicates
courses = ['History', 'Math', 'Physics','Chem', 'Bio']
print(courses)

# getting the length
print(len(courses))

# accessing individual elements
print(courses[1])

# last item
print(courses[-1])

# range of items
print(courses[0:2]) #the last index is not included
print(courses[:2]) #same thing

print(courses[2:]) # index 2 onwards

# list methods

# Add items
courses.append('Art')
print(courses)

# add to specific place
courses.insert(3, 'Tech') # 3 is the index you want it to be
print(courses)

# extend method
skillset = ['Code', 'Python']
# courses.insert(4, skillset)
# print(courses)
# print(courses[4]) #print a list

courses.extend(skillset)
print(courses)

# remove items
courses.remove('Math')
print(courses)

# removing the last item
popped = courses.pop()
print(popped)

# reverse
courses.reverse()
print(courses)

# sort
courses.sort()
print(courses)

nums = [23,454,56,34,1,3245,6345]
nums.sort() # ascending order
print(nums)

nums.sort(reverse=True) # descending order
print(nums)

# sorted function - it doesn't alter the original
sorted_courses = sorted(courses)

# min, max and sum
print(min(nums))
print(max(nums))
print(sum(nums))

# find values
print(courses.index('Chem'))

# check if value exist
print("Art" in courses)

# loop through values
for course in courses:
    print(course)


for index,course in enumerate(courses, start=1):
    print(index,course)

# lists to string
courses_str = ','.join(courses)
print(courses)
courses_str = ' '.join(courses)
print(courses_str)

# string to list
string = "Hello My Name Is Sam Wanyua"
str_list = string.split(' ')
print(str_list)

# Slicing lists and strings

my_list = [0,1,2,3,4,5,6,7,8,9]

print(my_list)

# slicing a range
print(my_list[0:6])
print(my_list[3:8]) 
# Alternatively
print(my_list[3:-2]) 

print(my_list[3:])
print(my_list[:-4])

# using a step
print(my_list[2:-1:2]) # it will skip 2 steps ie even value

print(my_list[2:-1:-1]) # []
print(my_list[-1:2: -2])

# reverse the entire list
print(my_list[::-1])

# strings
sample_url = 'http://coreymsfasds.com'
print(sample_url)

# reverse the url
print(sample_url[::-1])

# get top level domain
print(sample_url[-4:])

# print url without http
print(sample_url[7:])

# both without http or domain
print(sample_url[7:-4])

print(sample_url)


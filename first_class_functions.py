# first class function
'''
First class functions treat functions as first-class citizens
First class citizens/ first class objects -> is an entity that supports all the
operations generally available to other entities. Ex. being passed as arguments,
returned from a function, assigned to a variable
'''

# assigning functions to a variable
def square(x):
    return x ** 2

# f = square(5)
f = square

# print(f) # same thing
print(f(45)) 

# passing functions as arguments  -> HOF

def cube(y):
    return y ** 3

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(cube, [1,2,3,4,5])
print(squares)


#  returning functions as a result

def logger(msg):
    def log_message():
        print('Log', msg)

    return log_message
log_hi = logger('Hi')
log_hi() # this is a closure



def html_tag(tag):
    def wrap_text(msg):
        print(f"Enter your {tag} and  your {msg}")
    return wrap_text

print_hi = html_tag('Hi') # tag = 'Hi'
print_hi('guy') # msg = 'guy'










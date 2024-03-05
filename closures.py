# closure
''' 

In Python, a closure is a function object that has access 
to variables in its lexical scope, even when the function 
is called outside that scope. This allows the function to 
"remember" the values of those variables at the time it was 
defined, even if they are not present in memory when the 
function is executed. Closures are created when you have a 
nested function that references a variable from its containing 
(enclosing) function.

'''

def outer_func():
    message = "Hello"

    def inner_function():
        print(message)

    return inner_function

    # return inner_function()
# outer_func()

my_func = outer_func()
# print(my_func)
my_func()


# example 2
def ext_funct(msg):
    message = msg
    def int_funct():
        print(message)

    return int_funct

call_ext = ext_funct('I got closures')
call_ext()

# example 3
def nje(msf):
    def nde(txt):
        print(f"This is {msf} and with {txt}")
    return nde

out_fc = nje('Matumbo')
out_fc('Got it now')

# example 4
def cube(x):
    return x ** 3

def my_map(func, arg_list):
    results = []
    for i in range(1,12):
        results.append(func(i))

    return results
resut = my_map(cube, [23,32,34,234,345,56])
print(resut)

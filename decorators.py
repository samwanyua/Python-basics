
# first class functions
from typing import Any


def out_func():
    message = 'Hello you are learning closures and first class functions'
    def in_func():
        print(message)

    return in_func
final = out_func()
# print(final)
final()

# decorators - function that takes other functions as an argument, adds functionalit and returns another function

def decorator_function(original_func):
    def wrapper_function(*args, **kwargs):
        print(f"Wraper executed this before {original_func.__name__} function.")
        return original_func(*args, **kwargs) #is a decorator
    
    return wrapper_function

@decorator_function # same as 'display = decorator_function(display)'
def display():
    print("Display function ran")

@decorator_function
def display_info(name, age):
    print(f"My name is {name} and I am {age} years old!")

display_info("John Mutembei", 47)


display()

'''
@decorator_function
def display():
    print("Display function ran")

display()

Is the same as
display = decorator_function(display)

'''

'''
Here's the code before
***
def decorator_function(original_func):
    def wrapper_function():
        print(f"Wraper executed this before {original_func.__name__} function.")
        return original_func() #is a decorator
    
    return wrapper_function

def display():
    print("Display function ran")

decorated_display = decorator_function(display)
decorated_display() # execute wrapper_function which runs display function

'''


# decorators in classees
class decorator_class(object):
    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print(f"Call method executed this before {self.original_func.__name__} function.")
        return self.original_func(*args, **kwargs) #is a decorator

@decorator_class
def display():
    print("Display function ran")

@decorator_class
def display_info(name, age):
    print(f"My name is {name} and I am {age} years old!")

display_info("John Mutembei", 47)


display()



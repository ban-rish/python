# Decorator - it means if we have an existing function and we want to extend its capability 
# or change the structure of the existing function

def greet(name):
    return f"Hello, {name} !"
sayHello = greet
print(sayHello("Rish"))
print("*"*50)

# manual decorator example
def simpleDecorator(func):
    def wrapper():
        print("Something happening before Function Execution")
        func()
        print("Something happening after Function Execution")
    return wrapper

def sayHello():
    print("Hello")

decorator_sayHello = simpleDecorator(sayHello)
decorator_sayHello()
print("*"*50)

# "@" is used for using a decorator
@simpleDecorator
def sayHelloDecorator():
    print("Hello from decorator function")

sayHelloDecorator()
print("*"*50)

# another example with arguments and keyword arguments
def flexible_decorator(func):
    def wrapper(*args,**kwargs):
        print(f"calling function: {func.__name__} with args: {args} and keyargs: {kwargs}")
        result = func(*args,**kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

@flexible_decorator
def add_numbers(a,b):
    return a+b

@flexible_decorator
def concatenate_strings(s1, s2, separator = " "):
    return s1 + separator + s2

sum_result = add_numbers(2,3)
"""Add the numbers"""
print(f"result of sum is {sum_result}")
print("*"*50)

concat_result = concatenate_strings("HI", "Rishabh", separator= " - ")
"""Concat the Strings"""
print(f"result of concatenation is {concat_result}")
print("*"*50)

concat_result_default = concatenate_strings("HI", "Rishabh")
print(f"result of concatenation is {concat_result_default}")
print("*"*50)


# functools.wraps()
# This makes the decorator function look and behave more like the orignal preserving the 
# identity and documentation

# Simple Function
def my_function():
    """Docstring for my_function"""
    print("Executing my Function")

print("Orignal Function Metadata :")
print(f"name of the orignal function is {my_function.__name__}")
print(f"docString of the orignal function is {my_function.__doc__}")
print("*"*50)

# Define a basic decorator without **functools.wraps**
def basic_decorator_without_wraps(func):
    def wrapper_without_wraps():
        """Docstring for wrapper_without_wraps"""
        print("something is happening before the Function")
        func()
        print("something is happening after the Function")
    return wrapper_without_wraps
    
# Apply the basic decorator
@basic_decorator_without_wraps
def decorated_function_without_wraps():
    """Docstring for decorated_function_without_wraps"""
    print("Executing function decorated_function_without_wraps")

print(f"name : {decorated_function_without_wraps.__name__}")
print(f"docstring : {decorated_function_without_wraps.__doc__}")
print("*"*50)

import functools
# Define a basic decorator with **functools.wraps**
def basic_decorator_wraps(func):
    @functools.wraps(func)          #Apply functools.wraps here
    def wrapper_with_wraps(*args,**kwarsgs):
        """Docstring for wrapper_with_wraps"""
        print("something else is happening before")
        result = func(*args,**kwarsgs)
        print("something else is happening after")
        return result
    return wrapper_with_wraps
    
# Apply the new decorator
@basic_decorator_wraps
def decorated_function_with_wraps():
    """Docstring for decorated_function_with_wraps"""
    print("Executing function decorated_function_with_wraps")

print(f"name : {decorated_function_with_wraps.__name__}")
print(f"docstring : {decorated_function_with_wraps.__doc__}")


# another example 

import time

def time_complex(func):
    @functools.wraps(func)
    def wrapper_time_complex(*args,**kwargs):
        """Docstring for wrapper_time_complex"""
        start_time = time.time()

        result = func(*args,**kwargs)

        end_time = time.time()

        time_taken = end_time - start_time

        print(f"Time taken by function {func.__name__} is {time_taken}")

        return result
    return wrapper_time_complex

@time_complex
def calculate(duration, multiplier):
    """Docstring for calculate"""
    time.sleep(duration)
    return duration*multiplier

mul_result_1 = calculate(2,4)
print(f"mul_result_1 result is {mul_result_1}")

mul_result_2 = calculate(3,4)
print(f"mul_result_2 result is {mul_result_2}")

mul_result_3 = calculate(1,4)
print(f"mul_result_3 result is {mul_result_3}")
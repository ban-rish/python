# "def" is the keyword for defining the Function
# "greet" is the function name 
# by "greet()" we are calling the Function 
# in python all the lines would be executed one by one 
# if we call a function before defining it then it would not work 

# function without any variable 
def greet():
    print("hello")
greet()
print('-'*50)

# scope of variable is global or local
# we can overwrite functions as mentioned in below code
# in below code "l_var" is not accessible outside the function and greet function is overwritten
g_var = 10
def greet():
    l_var = 5
    print(g_var,l_var)
# print(g_var,l_var)
greet()
print('-'*50)

# overloading of a function is not possible in python based on parameters
def greet(n):
    print("Hello",n)
greet("Rish")
print('-'*50)

# if user does not pass anything then we can write default value to it
def defaultGreet(name = 'PC'):
    print("Hello", name)
defaultGreet()
print('-'*50)

def sumb(a=0,b=0):
    print(a,b,a+b)
sumb(10,5)
sumb(b=15, a=10)
sumb(b=15)
print('-'*50)

# take return from a function 
# The return statement ends a function and sends a value back to the caller. 
# It can return any data type, multiple values (packed into a tuple), or None if no 
# value is given.
def arithmatic(a=1,b=1):
    return a*b, a+b, a-b
# here "var" is of type tuple 
var = arithmatic(1,2)
mult, add, sub = arithmatic(10,5)
print(var, mult, add, sub)
print('-'*50)

# calling function inside the function 
lst1 = [1,2,3,4,5]
def sq(lst):
    return [i**2 for i in lst]
def cu(lst):
    return [i**3 for i in lst]
def add_sq_cu(lst):
    lst2 = sq(lst1)
    lst3 = cu(lst1)
    return [lst2[i]+lst3[i] for i in range(len(lst1))]
lst4 = add_sq_cu(lst1)
print(lst4)
print('-'*50)

# aribitrary non key and Key arguments 
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

# Function call with both types of arguments
myFun('Hey', 'Welcome',"Rishabh" , first='Geeks', mid='for', last='Geeks')
print('-'*50)


# an anonymous function means that a function is without a name. 
# here lambda keyword is used to create anonymous functions 
cube_l = lambda x : x*x*x  # with lambda
print(cube_l(7))
print('-'*50)

# When we pass them to a function, the behavior depends on whether the object is mutable 
# (like lists, dictionaries) or immutable (like integers, strings, tuples).
# Mutable objects: Changes inside the function affect the original object.
# Immutable objects: The original value remains unchanged
# Function tries to modify an integer
def myFun2(x):
    x = 20

a = 10
myFun2(a)
print(a)     # integer is not modified
print('-'*50)

# A recursive function is a function that calls itself to solve a problem. 
# It is commonly used in mathematical and divide-and-conquer problems.
def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
      
print(factorial(4))
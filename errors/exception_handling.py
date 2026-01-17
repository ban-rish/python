# basic exception Handling
x =10
try:
    print("1")
    print(x/0)
    print("2")
except:
    print("Error Occured!")
print("*"*50)

# Exception with Specific Errors
# we can have try with Multiple Except blocks
try:
    print(int("ncj"))
    print(x/0)
except ZeroDivisionError:
    print("Put something other than Zero in the divisor")
except:
    print("Unknown Error Occured")
print("*"*50)

# we can also have "else" with "try" block, which will execute if no error is captured
# we have "Finally" block as well which will always execute if code has error or not
try:
    num1, num2 = 10,0
    print(int("3.14"))
except ZeroDivisionError as ze:
    print(f"Error is {ze}")
except ValueError as ve:
    print(f"Error is {ve}")
except Exception as ee:
    print(f"Error is {ee}")
else:
    print("program is successfully executed")
finally:
    print("Program Terminated")
print("*"*50)

# catching multiple exceptions
a = ["10", "twenty", 30]  # Mixed list of integers and strings
try:
    total = int(a[0]) + int(a[1])  # 'twenty' cannot be converted to int
    
except (ValueError, TypeError) as e:
    print("Error", e)
    
except IndexError:
    print("Index out of range.")
print("*"*50)

# We raise an exception in Python using the raise keyword followed by an instance 
# of the exception class that we want to trigger.
# Syntax = raise ExceptionType("Error message")
def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except ValueError as e:
    print(e)
print("*"*50)

# we can create custom exceptions by defining a new class that inherits from Python’s 
# built-in Exception class.

class AgeError(Exception):
    pass

def set(age):
    if age < 0:
        raise AgeError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except AgeError as e:
    print(e)
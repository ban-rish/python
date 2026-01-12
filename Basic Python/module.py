# to break code into different modules for better utilization 
# here in the below code all functions in the function.py are imported into module.py
# we can directly use all the functions from function.py
# pyhton has huge library base for modules we can just import them and use it

# Import From Module: This allows importing specific functions, classes, or variables 
# rather than the whole module.
from math import sqrt, factorial

# Import All Names: * imports everything from a module into the current namespace.
from function import *

# Import With Alias: You can shorten a module’s name using as.
import math as m
print(m.pi)

lst = [1,2,4,5,6]
print(greet("Rishabh"))
print(sumb(10,5))
print(arithmatic(10,5))
print(add_sq_cu(lst))
print(myFun('Hey', 'Welcome',"Rishabh" , first='Geeks', mid='for', last='Geeks'))
print(cube_l(7))
print(factorial(7))

# Python provides several kinds of modules. Each type plays a different role in 
# application development.

# Built-in Modules: These come bundled with Python and require no installation - 
# e.g., math, random, os.
import random
print(random.randint(1, 5))

# User-Defined Modules: These are modules you create yourself, such as function.py.


# External (Third-Party) Modules: These modules are installed using pip - 
# e.g., NumPy, Pandas, Requests.
import requests
r = requests.get("https://example.com")
print(r.status_code)

# Package Modules: A package is a directory containing multiple modules, 
# usually with an __init__.py file.

# Python searches for modules in a predefined list of directories known as the 
# module search path. You can view this list using sys.path.
import sys
for p in sys.path:
    print(p)
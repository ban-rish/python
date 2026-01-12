# In Python, a library is a group of modules that contain functions, classes and methods 
# to perform common tasks like data manipulation, math operations, web scraping and more.

# here we will discuss about Math, Random, Collection, Strings and dateTime Libraries

# there are three ways to import the libraries
# 1. Import the entire library: import library_name for example, import math
# 2. Import a specific function or class: from library_name import function_name for example, 
# from math import sqrt
# 3. Import a library with an alias: import library_name as alias for example, 
# import pandas as pd

# import math library
import math
x = 13.21
print(math.ceil(x))
print(math.floor(x))
print(math.trunc(x))
print('-'*50)

y = 3
print(math.exp(y))
print(math.log10(y))
print('-'*50)

z = 90
print(math.sin(z))
print(math.cos(z))
print(math.tan(z))
print('-'*50)

print(math.pi)
print(math.e)
print(math.factorial(10))
print('-'*50)


# Random Library
import random
random.seed(37)
print(random.random())          # print any random float value b/w 0 to 1
print(random.randint(1,100))    # print random integer b/w the given values
print(random.choice([1,2,3,4,5,6]))     #print random number from the choices
print(random.sample([1,2,3,4,5,6],2))   # here we will take any 2 random values
print(random.uniform(1.0,10.0))       # here a random float would be genrated from 1.0 to 10.0
print('-'*50)

# date and Time Library
import datetime

print(datetime.datetime.now())      # to print date Time of now
print(datetime.datetime(2026,12,2,12,32,00))    #to print a specific date and Time
print(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))    # to write date in a specific format
date_1 = datetime.datetime(2034,12,2,12,32,00)
date_2 = datetime.datetime.now()
print(date_1-date_2)
print('-'*50)

# collections library
from collections import Counter, defaultdict, OrderedDict
lst = [1,2,3,2,4,2,4,2]
print(Counter(lst))             # here it will print key as number from list and value as number of counts in dictionary
print('-'*50)

d = defaultdict(int)        # here we have default Key and value, means if a key is not defined in the dictionary then also we can access its elements
d['a'] += 5
print(d) 
print('-'*50)

d1 = OrderedDict()
d1['a'] = 1         # here values are added in the order of adding elements in the Dictionary
d1['b'] = 2
print(d1)
print('-'*50)

# String Libraries
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print('-'*50)

print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print('-'*50)

print(string.punctuation)       # for all the special Characters
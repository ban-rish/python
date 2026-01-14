# lambda is replacement for defining the function
# use of Lambda  is not recomended for complex functions but small functions only

def square(x):
    return x**2
print(square(4))
print('*'*50)

# to write this code as a lambda Function
# Syntax = lambda arguments : expression

square2 = lambda x : x**2
print(square2(43))
print('*'*50)

# there are many functions inside lambda function 
# 1. lambda

li = [lambda arg = x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())
print('*'*50)

# for multiple returns through Lambda function
calc = lambda x, y: (x + y, x * y)
res = calc(3, 4)
print(res)
print('*'*50)

# 2. Map - if we have a data structure where we want to perform some operations
# it applies a given function to each element of an iterable (list, tuple, set, etc.) 
# and returns a map object (iterator).

# Syntax - map(function, iterable,..)

s = ['1', '2', '3', '4']
res = map(int, s)
print(list(res))
print('*'*50)

fruits = ['apple', 'banana', 'cherry']
res = map(str.upper, fruits)
print(list(res))
print('*'*50)

s = ['  hello  ', '  world ', ' python  ']
res = map(str.strip, s)
print(list(res))
print('*'*50)

# calculate Fahrenheit from Celcius
celsius = [0, 20, 37, 100]
fahrenheit = map(lambda c: (c * 9/5) + 32, celsius)
print(list(fahrenheit))
print('*'*5)

n = [1,3,4,65,232,1232]
square3 = list(map(lambda x : x**2, n))
print(square3)
print('*'*50)

# map() with multiple iterables
a = [1, 2, 3]
b = [4, 5, 6]
res = map(lambda x, y: x + y, a, b)
print(list(res))
print('*'*50)

# 3. Filter - filter() function is used to extract elements from an iterable 
# (like a list, tuple or set) that satisfy a given condition.
# it also works with Lambda with a condition

# syntax - filter(function, iterable)
# function: tests each element and if return, True - Keep the element, if False - Discard the element
# iterable: Any iterable (list, tuple, set, etc.).

n = [1,3,4,65,232,1232]
square4 = list(filter(lambda x : x%2 ==0, n))
print(square4)
print('*'*50)

# filter without lambda   
ls1 = [1,2,3,4,5,6,7,8,9]
def isEven(n):
    return n%2==0
print(list(filter(isEven,ls1)))
print('*'*50)

# filtering and Transforming data 
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)
c = map(lambda x: x * 2, b)
print(list(c))

# filtering on strings
a = ["apple", "banana", "cherry", "kiwi", "grape"]
b = filter(lambda w: len(w) > 5, a)
print(list(b))

# removing all falsy values (empty string, None and 0) and keeps only truthy ones
L = ["apple", "", None, "banana", 0, "cherry"]
A = filter(None, L)
print(list(A))

# 4. reduce - This performs a repetitive operation over the pairs of the iterable. 
# The reduce() function belongs to the functools module.
from functools import reduce
n = [1,3,4,65,2,1]
reduce1 = reduce(lambda x,y: x+y, n)
print(reduce1)
print('*'*50)

# 5. zip function is used to combine two or more iterables or zip somethings as single entity
list1 = ["a","b","c"]
list2 = [1,2,3]
print(list(zip(list1,list2)))       # output - [('a', 1), ('b', 2), ('c', 3)]
print('*'*50)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print([list(row) for row in zip(matrix)])   # output = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

# '*' here represents unzipping means reverse of zipping. 

print([list(row) for row in zip(*matrix)])  # output = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print([list(row) for row in zip(*[list(row) for row in zip(*matrix)])])
print('*'*50)

lst_1 = [2,4,6]
lst_2 = [1,3,5]
print(sum([row[0]*row[1] for row in zip(lst_1,lst_2)])) # returns the dot product and dot product sum
print('*'*50)

# if the length of two iterables are different
names = ['Hiro', 'Mila', 'Tariq']
scores = [88, 94]
res = zip(names, scores)
print(list(res))        # output - [('Hiro', 88), ('Mila', 94)]
print('*'*50)

# Unzipping example 
a = [('Apple', 10), ('Banana', 20), ('Orange', 30)]
fruits, quantities = zip(*a)

print("Fruits:", fruits)
print("Quantities:", quantities)
print('*'*50)

# combine dictionary keys and values 
d = {'name': 'Felix', 'age': 27, 'grade': 'A'}
keys = d.keys()
values = d.values()

res = zip(keys, values)
print(list(res))
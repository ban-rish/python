# lambda is replacement for defining the function
# use of Lambda  is not recomended for complex functions but small functions only

def square(x):
    return x**2
print(square(4))
print('*'*50)

# to write this code as a lambda Function
square2 = lambda x : x**2
print(square2(43))
print('*'*50)

# there are many functions inside lambda function 
# 1. lambda
# 2. Map - if we have a data structure where we want to perform some operations
n = [1,3,4,65,232,1232]
square3 = list(map(lambda x : x**2, n))
print(square3)
print('*'*50)

# 3. Filter - it also works with Lambda with a condition
n = [1,3,4,65,232,1232]
square4 = list(filter(lambda x : x%2 ==0, n))
print(square4)
print('*'*50)

# 4. reduce 
from functools import reduce
n = [1,3,4,65,2,1]
reduce1 = reduce(lambda x,y: x+y, n)
print(reduce1)
# Tuples can hold elements of different data types.
# The main characteristics of tuples are being ordered, heterogeneous and immutable.


# Tuple Initialization
tup_1 = (1,2,12,43,1,2)
print(tup_1)
print('-'*50)

#Accessing Tuple elements
print(tup_1[0])
# slicing elements in Tuple
print(tup_1[1:3])
print('-'*50)

# tuple concatenation
tup_2 = (3,43,1,12)
tup = tup_1 + tup_2
print(tup)
# length of the tuple
print(len(tup))
print('-'*50)

# iterating through tuple
for i in tup:
    print(i, end = " ")
print()
print('-'*50)

# Checking the element in the Tuple 
print(1 in tup)
print(4 in tup)
print(11 in tup)
print('-'*50)

# count of a value in Tuple
print(tup)
print(tup.count(4))
print('-'*50)

# to find the index of an element
print(tup)
# print(tup.index(4))
print(tup.index(12))
print('-'*50)

# Multiply the Tuple 
print(tup*3)
print('-'*50)

# Creating a Tuple with nested tuples
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')
tup3 = (tup1, tup2)
print(tup3)
print('-'*50)

# Tuple unpacking
tup = ("Geeks", "For",1,2,3, "Geeks")
# This line unpack values of Tuple1
a, *b, c = tup
print(a)
print("Here b store elements as list ",b)
print(c)
print('-'*50)

# delete a tuple
tup = (0, 1, 2, 3, 4)
del tup
# print(tup)

# set                   tuple                   list                dictionary
# {}                    ()                      []                  {}
# Mutable               Immutable               Mutable             Mutable
# Unordered             Ordered                 Ordered             Ordered
# No Duplicacy          Duplicacy               Duplicacy           Values can be Duplicate
# Keyword - set         tuple                   list                dict
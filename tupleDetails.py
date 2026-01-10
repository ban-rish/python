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

# set                   tuple                   list                dictionary
# {}                    ()                      []                  {}
# Mutable               Immutable               Mutable             Mutable
# Unordered             Ordered                 Ordered             Ordered
# No Duplicacy          Duplicacy               Duplicacy           Values can be Duplicate
# Keyword - set         touple                  list                dict
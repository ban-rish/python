# Set initialized with curly Brackets "{}", Tuples with "()"
# Set are Mutable in Nature we can add, delete or update but Tuple are Immutable
# Set does not allow duplicate elements but Tuple can have duplicate elements
# Order is not maintained in Sets but it is maintained in Tuple
# Set are used for maintaining Uniqueness and Tuple are used for unpacking and maintain Order

# creation of a set
my_set = {1,2,3,4,5,6}
print(my_set)
print(type(my_set))
print('-'*50)

#Addition of an element
my_set.add(7)
print(my_set)
print('-'*50)

#Pop
popedEle = my_set.pop()
print(my_set)
print(popedEle)
print('-'*50)

# remove particular element
print(my_set)
my_set.remove(3)
my_set.discard(2)
print(my_set)
print('-'*50)

#iteration on the Set
for i in my_set:
    print(i)
print('-'*50)

# check if value is present in the set or not
print(my_set)
print(2 in my_set)
print(3 in my_set)
print(4 in my_set)
print('-'*50)

# set operations
set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8}
print("Union Operation : ", set_1 | set_2)
print("Intersection Operation : ", set_2 & set_1)
print("Difference Operation : ", set_2 - set_1)
print("Symmetric Difference : ", set_1 ^ set_2)
print('-'*50)
# Above mentioned all operations are present in Set Data Structure only not in List or Tuple

# clearing the set
print(my_set)
my_set.clear()
print(my_set)
print('-'*50)
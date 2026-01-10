# Set initialized with curly Brackets "{}", Tuples with "()"
# Set are Mutable in Nature we can add, delete or update but Tuple are Immutable
# Set does not allow duplicate elements but Tuple can have duplicate elements
# Order is not maintained in Sets but it is maintained in Tuple hence we cannot access items using indexes in sets as we do in lists
# Set are used for maintaining Uniqueness and Tuple are used for unpacking and maintain Order
# Set Internally use hashing that makes set efficient for search, insert and delete operations. It gives a major advantage over a list for problems with these operations.

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
my_set.remove(8)    # if element is not present while using remove then it will throw an error
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

# typecasting list to set
s = set(["a", "b", "c"])
s.add("d")
print(s)
print('-'*50)

# a set can store a mixture of string, integer, boolean, etc datatypes.
s = {"Geeks", "for", 10, 52.7, True}
print(s)
print('-'*50)

# Frozen sets in Python are immutable objects that only support methods and operators that 
# produce a result without affecting the frozen set or sets to which they are applied.
fs = frozenset(["e", "f", "g"])
print("\nFrozen Set")
# Uncommenting below line would cause an error
# fs.add("h")
print(fs)


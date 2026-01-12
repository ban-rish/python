# Values in a dictionary can be of any data type and can be duplicated, 
# whereas keys can't be repeated and must be immutable.

# Keys are case sensitive which means same name but different cases of Key will be treated distinctly.
# Keys must be immutable which means keys can be strings, numbers or tuples but not lists.
# Duplicate keys are not allowed and any duplicate key will overwrite the previous value.
# Internally uses hashing. Hence, operations like search, insert, delete can be performed in Constant Time.
# From Python 3.7 Version onward, Python dictionary are Ordered.

# initialising the dictionary syntax
dict = {1:'a',2:'b',3:'c',4:'d',5:'d',6:'f',3:'g'}
print(dict)
dict1 = {'a':1,2:'b',3:'c',4:'d',5:'d',6:'f',3:'g','3':'h'}
print(dict1)
print('-'*25)

#Accessing the elements
print(dict1.get('3'))
print(dict1[3])
print('-'*25)

# adding and updating key value pairs
dict[7] = 'i'
print(dict)
print('-'*25)
dict[7] = 'j'
print(dict)
print('-'*25)
del dict[7]
print(dict)
print('-'*25)

# cleaning the dictionary 
print(dict)
dict.pop(1)
print(dict)
dict.clear()
print(dict)
print('-'*25)

# We can iterate over keys [using keys() method] , values [using values() method] or 
# both [using item() method] with a for loop.

# iteration of keys and values
print(dict1.keys())
print(dict1.values())
for i in dict1.keys():
    print(dict1[i],i) 
print('-'*25)

print(dict1.items())
print('-'*25)

for k,v in dict1.items():
    print(k,v)
print('-'*25)

# check if key is present on the dictionary
print(2 in dict1)
print(1 in dict1)
print('-'*25)

# update the dictionaries
# dict = {1:'a',2:'b',3:'c',4:'d',5:'d',6:'f',3:'g'}
# dict1 = {'a':1,2:'b',3:'c',4:'d',5:'d',6:'f',3:'g','3':'h'}
dict = {1:'a',2:'b',3:'c',4:'d',5:'d',6:'f',3:'g'}
dict1.update(dict)
print(dict1)
print('-'*25)

# merge two dictionary
dict_1 = {1:2,2:3,3:4,4:5}
dict_2 = {9:8,8:7,7:6,6:5}
for k,v in dict_2.items():
    dict_1[k] = v
print(dict_1.items())
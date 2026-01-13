# in Multi Dimensional Dictionary we can have value as another Data Structure type 
# it can be List, set, dictionary, tuple

#example 
dict1 = {1:{"name":"Rishabh","number":8329839},
         2:{"name":"Sam","number":232323322},
         3:{"name":"Buddy","number":33254532}}
print(dict1)
print("-"*50)

#Accessing the elements of the dictionary
print(dict1[1]['name'])
print("-"*50)

#Adding, Updating Dictionary
print(dict1)
dict1[4] = {"name":"Sam","number":7485748548}   #Adding the value
dict1[2]['name'] = "Saumya" #updation
print(dict1)
print('-'*50)

# Deleting Dictionary
del dict1[4]
print(dict1)
print('-'*50)

#iterating through the Dictionary
for i in dict1.keys():
    print(i, dict1[i]['name'], dict1[i]['number'])
print('-'*50)

#more deep into Multi dimensional Dictionary
data1 = {1:{"name":"Rishabh","number":8329839,"marks":{"Math":50,"Science":48,"Comp":49}},
         2:{"name":"Sam","number":232323322,"marks":{"Math":3,"Science":8,"Comp":4}},
         3:{"name":"Buddy","number":33254532,"marks":{"Math":43,"Science":8,"Comp":29}}}

print(data1)
print('-'*50)

#accessing elements here 
for j in data1.keys():
    print(j, data1[j]['name'], data1[j]['marks']['Math'])
print('-'*50)

#Dictionary comprehension
# for dictionary we need to write comprehensions in curly braces
# Syntax => {key: value for (key, value) in iterable}
dict2 = {i:i**2 for i in range(1,6)}
print(dict2)
print('-'*50)

# if else condition in comprehension
dict3 = {i:i**3 for i in range(1,11) if i%2==0}
print(dict3)
print('-'*50)

# convert from List to Dictionary
lst1 = ['Apple',"Boy","Cat"]
fruits = {lst1[j]:len(lst1[j]) for j in range(len(lst1))}
print(fruits)
print('-'*50)

# convert from String to Dictionary
strdict = {"num_"+str(r):r for r in range(15)}
print(strdict)
print('-'*50)

# string another example
sDict = {x.upper(): x*3 for x in 'coding'}
print (sDict)
print('-'*50)

# Condition based on Values
multiple3 = {k:v for k,v in strdict.items() if v%3==0}
print(multiple3)
print('-'*50)

# make dictionary from 2 lists
lst2 = [1,2,3]
lstdict = {lst1[i]:lst2[i] for i in range(len(lst1)) if len(lst1) == len(lst2)}
print(lstdict)
print('-'*50)

# matrix of list to Dictionary
# here from the below example it is clear that Key is not a int, string but Tuple
matrix = [[1,2,3],[4,5,6],[7,8,9]]
finalDict = {(i,j):matrix[i][j] for i in range(3) for j in range(3)}
print(finalDict)
print('*'*50)

# we have two lists named keys and value and we are iterating over 
# them with the help of zip() function.
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]  
myDict = { k:v for (k,v) in zip(keys, values)}  
# We can use below too myDict = dict(zip(keys, values))  
print (myDict)
print('-'*50)

# we are using the fromkeys() method that returns a dictionary with specific 
# keys and values
dic=dict.fromkeys(range(5), True)
print(dic)
print('-'*50)
# List is the collection which can store different type of data, it is represented via square brackets [] and values are comma seperated.
lst = [1,1.4,True,'Rishabh']
print(lst)

#Access element through Indexing
print(lst[0])
print(lst[-3])
print('*'*25)

# Modify the list
print(lst)
lst[3] = 'Sam'
print(lst)
print('*'*25)

# reverse and slicing of a List
print(lst[::-1])
print(lst.reverse)
print(lst[::-2])
print(lst[1:3])
print('*'*25)

# append value and remove value in existing list 
lst.append('Ani')
print(lst)
lst.remove('Ani')
print(lst)
print('*'*25)

# length of a list 
print(len(lst))
print('*'*25)

# sorting in a list 
lst2 = [1,3,43,3232,34,4,655]
print(sorted(lst2))
print(sorted(lst2,reverse=True))
lst2.insert(0, 5)               #insert at specified location
print("After insert(0, 5):", lst2) 
print('*'*25)
lst2.clear()                    #to clear list
print("After clear():", lst2)

#count the occurance
print(lst.count(1))
print(lst)
print('*'*25)

#add multiple values in the list 
lst.extend([1,232,432,'csc'])
print(lst)
print('*'*25)

# find minimum and maximum value in the list 
lst2=[3.32,433.12,.4,4343.1]
print(max(lst2))
print(min(lst2))
print('*'*25)

#iterating the list
print(lst)
for i in lst:
    print(i)
print('*'*25)
for i in range(len(lst)):
    print(i,lst[i])
print('*'*25)

# reverse the list
for i in range(len(lst)-1,-1,-1):
    print(i,lst[i])
print('*'*25)

# remove(): Removes the first occurrence of an element.
# pop(): Removes the element at a specific index or the last element if no index is specified.
# del statement: Deletes an element at a specified index.

a = [10, 20, 30, 40, 50]

a.remove(30)  
print("After remove(30):", a)
print('*'*25)

popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a) 
print('*'*25)

del a[0]  
print("After del a[0]:", a)
print('*'*25)

#list comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)
print('*'*25)

# Empty list 
numbers = (4,5,1,2,3,5)
list1 = []
for i in range(len(numbers)):
    list1.append(numbers[i]*2)
number = tuple(list1)
print(number)
print('*'*25)

# check index 
print(list1)
list1 += [10]
print(list1)
print('*'*25)

li = ['a','b','c','d']
print("".join(li))      #Output = abcd
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
print('*'*25)

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

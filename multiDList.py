lst = [[0,1,2],[3,4,5],[6,7,8],9]
print(lst)

#accessing specific element of the List
print(lst[0])
print(lst[1][1])
print(lst[2][2])
print('-'*25)

#modifing specific element of the List
print(lst)
lst[1][1] = ['Rish',29]
print(lst)
print('-'*25)

# slicing operator for a list
print(lst[1:3:2])
print(lst[::-1])
print('-'*25)

#appending, deleting and removing the value from the list
lst.append(['bcdj',32])
print(lst)
lst.remove(lst[0])
print(lst)
del lst[len(lst)-1]
print(lst)
print('-'*25)

#reversing the list
lst1 = [[1,2,3],[4,5,6],[7,8,9]]
print(lst1[::-1])
print('-'*25)

#accessing all elements in the list 
for i in lst1:
    for j in i:
        print(j,end=' ')
print()
print('-'*25)

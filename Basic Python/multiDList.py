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

# list comprehension
#syntax of List Comprehension - [expression for item in iterable if condition]
lst2 = [1,2,3,4,5,6]
print(lst2)
lst2 = [i**2 for i in lst2]
print(lst2)
print('-'*25)

# print first 10 even numbers
print([i for i in range(20) if i%2==0])
print('-'*25)
#here first for loop would be executed then if condition after which value of "i"
#would be printed

# table of a number
print([i for i in range(20, 201) if i%20==0])
print('-'*25)

# multidimensional list comprehension 
print([[i for i in range(7)] for j in range(5)])
print('-'*25)
#here first loop defines the columns and second loop defines the rows

# printing values in using comprehension
lst = [[0,1,2],[3,4,5],[6,7,8]]
print([num for row in lst for num in row])
#here row represent [0,1,2],[3,4,5],[6,7,8] and num represent element in each row

#Creating a Multidimensional Zero Matrix
m, n = 4, 5
mat = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(0)
    mat.append(row)
print(mat)

#access elements using Index-Based Nested Loops
a = [[2, 4, 6, 8], 
     [1, 3, 5, 7], 
     [8, 6, 4, 2], 
     [7, 5, 3, 1]]     
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()

#reverse Multi Dimensional List
a = [[2,4,6],[3,6,9]]
a[1].reverse()   # reverse second row
print(a)
a.reverse()      # reverse row order
print(a)
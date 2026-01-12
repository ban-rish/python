# assignment of the variables
a=10
x=0
y=0
z=0
print(a,x,y,z)
print
print('-'*20)

# same value to multiple variables
x = y = z = 10
print(a,x,y,z)
print('-'*20)

# different value for different variable in single line
a , x , y , z = 38, 'ndcks', 32.232, True
print(a,x,y,z)
print('-'*20)

# taking values from the list
data = 38, 'ndcks', 32.232, True
print(data)
print(type(data))
a,x,y,z = data
print(a,x,y,z)
print('-'*20)

# take input from the user
n=input("enter your name : ")
print("String which is entered is "+n)
print('-'*20)

first = int(input("Enter first number : "))
second = int(input("Enter Second Number : "))
print(first+second)
print(first%second)
print(first-second)
print(first/second)
print(first*second)
print(first**second)
print(first//second)
print('-'*20)

# Arithmatic Operator with Assignment
n=10
n+=1
print(n)
n-=1
print(n)
n*=2
print(n)
n/=2
print(n)
n**=2
print(n)
n//=2
print(n)
n%=2
print(n)
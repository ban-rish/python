# if else practise code
n = int(input("Enter a number : "))
if(n>=0):
    print(n,"it is a +ve number")   
else:
    print(n,"it is a -ve number")
print("_"*20)


if(n==0):
    print(n,"it is zero")
elif(n>0):
    print(n,"it is a +ve number")
else:
    print(n,"it is a -ve number")
print("_"*20)


if(n%5 == 0):
    if(n%3 == 0):
        print(n,"is divisible by both 5 and 3")
    else:
        print(n,"is divisible by 5 only")
else:
    print(n,"is not divisible by 5")
print("_"*20)

if((n%5 == 0) and (n%3==0)):
    print(n,"second divisible by both 5 and 3")
elif((n%5 == 0) or (n%3==0)):
    if(n%5 == 0):
        print(n,"second divisible by 5")
    else:
        print(n,"second divisible by 3")
else:
    print(n,"second not divisible")

a = int(input("Enter the first number "))
b = int(input("Enter the second number "))
us = input("enter the operation '+' or '-'")

if(us == '+'):
    print(a+b)
elif(us == '-'):
    print(a-b)
else:
    print("invalid operation")
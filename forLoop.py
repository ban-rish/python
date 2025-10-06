# print table of a number
n = int(input("Enter the Number - "))
for i in range(1,11):
    if(i==0):
        continue
    else:
        print(n, '*', i, '=', n*i)

# print table in 2 lines
for i in range(n, (n*10)+1, n):
    print(i)

# nested for loop
for i in range(1,7):
    for j in range(1,7):
        print(i, j)

# probability of finding a number when rolling three dices
for num in range(3,19):
    n=0
    for i in range(1,7):
        for j in range(1,7):
            for k in range(1,7):
                if (i+j+k == num):
                    n+=1
    print(num, round((n/216)*100,2))
            
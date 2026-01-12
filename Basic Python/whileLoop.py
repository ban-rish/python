i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue        #Continue Statement returns the control to the beginning of the loop.
    print(a[i])
    i += 1
print('-'*25)
i = 0
while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        break           #Break Statement brings control out of the loop.    
    print(a[i])
    i += 1
print('-'*25)
i = 0
while i < len(a)-1:
    if a[i] == 'e' or a[i] == 's':
        i += 1
        pass           #Python pass statement to write empty loops
    print(a[i])
    i += 1
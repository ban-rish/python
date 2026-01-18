fd = open(r"C:\Users\bansa\Personal\github\python\fileHandling\data.txt",'r')
txt = fd.read()
fd.close()
print(txt)
print("*"*50)

# replace numbers in format "[1]" with empty string
for i in range(3,16):
    pattern = '['+str(i)+']'
    txt = txt.replace(pattern,'')

print(txt)

# for removing all the special characters
for i in "!@#\$%^":
    txt = txt.replace(i , "")
print(txt)
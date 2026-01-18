# Appending in an already existing file 
# "\n" is used here to move to next line 

f1 = open("myfile.txt", "a") 
f1.write("Today \n")
f1.close()

f1 = open("myfile.txt", "r")
print("Output of Readlines after appending")
print(f1.readlines())
print()
f1.close()

f1 = open("myfile.txt", "w")  
f1.write("Tomorrow \n")
f1.close()

f1 = open("myfile.txt", "r")
print("Output of Readlines after writing")
print(f1.readlines())
print()
f1.close()

# There are two ways to write in a file:

# 1. Using write() - Inserts the string str1 in a single line in the text file.
# Syntax - File_object.write(str1)
f1 = open("Employees.txt", "w") 

for i in range(3): 
    name = input("Enter the name of the employee: ") 
    f1.write(name) 
    f1.write("\n") 
	
f1.close() 
print("Data is written into the file.")

# to create an empty file 
fd = open("Dump.txt",'w')
fd.close()

# 2. Using writelines() - For a list of string elements, each string is inserted in text file. Used to insert multiple strings at a single time.
# Syntax - File_object.writelines(L) for L = [str1, str2, str3]
f2 = open("Multiple_Employees.txt", "w") 
lst = [] 
for i in range(3):
    name = input("Enter the name of the employee: ")
    lst.append(name + '\n') 
	
f2.writelines(lst) 
print(lst)
f2.close() 
print("Data is written into the file.") 

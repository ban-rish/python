# Python can handle two types of files:
# Text files: Each line of text is terminated with a special character called EOL (End of Line), which is new line character ('\n') in Python by default.
# Binary files: There is no terminator for a line and data is stored after converting it into a machine-understandable binary format.

# syntax for opening a file 
# File_object = open(r"File_Name","Access_Mode")

# for reading a file there are three methods in python
# 1. Using read() - File_object.read([n])
# 2. Using readline() - it reads one line only
# Syntax - File_object.readline([n])
# 3. Using readlines() - read all the lines and return them as each line a string element
# Syntax - File_object.readlines()

# "\n" is used when we want to move to next line 
# "\t" (Tab Character): Represents indentation.

# Files opened in "r" mode are read-only, so attempting to write raises an UnsupportedOperation error.

# If a file is not closed, buffered data may not be flushed to disk, leading to incomplete or unsaved writes.

f1 = open("myfile.txt", "w")  
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

f1.write("Hello \n")          
f1.writelines(L)             
f1.close()                   

f1 = open("myfile.txt", "r+") 

print("Output of read():")
print(f1.read())              
print()

f1.seek(0)                    
print("Output of readline():")
print(f1.readline())          
print()

f1.seek(0)
print("Output of read(9):")
print(f1.read(9))             
print()

f1.seek(0)
print("Output of readline(9):")
print(f1.readline(9))         
print()

f1.seek(0)
print("Output of readlines():")
print(f1.readlines())         
print()

f1.close()


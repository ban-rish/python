# Errors
# Errors are problems in a program that causes the program to stop its execution. 
# On the other hand, exceptions are raised when some internal events change the program's normal flow. 

# 1. Syntax Errors - 
# 2. Run Time Error - error is not present at compile time but run time
# 3. Logical Error - where code will run but the logic of code is not correct
# 4. Type Error - adding String and integer
# 5. Index Error - accessing element outside the index range
# 6. Key Error - when key is not present and we try to access it
# 7. Attribute Error - where we are not using correct attribute or correct methods as per attribute
# 8. Indentation Error - when spacing is not proper
# 9. Import Error - occurs when we try to import something and it is not present
# 10. Value Error - Typecasting string "abc" to integer

# Error Handling
# mechanisms to handle errors and exceptions using the try, except, and finally blocks.
try:
    print("code start")
    print(1 / 0)  

except:
    print("an error occurs")

finally:
    print("GeeksForGeeks")
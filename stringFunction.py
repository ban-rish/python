#string functions

#concatination
print("Hi" + " " + "there")
print("-----------------------")

#replication of String
print("Hi " *5)
print("-----------------------")

# find String Leangth
print(len("Hi there Saumya"))
print("-----------------------")

#String Slicicng
print("Saumya Bansal"[0])
print("Saumya"[-6])
print("Saumya Bansal"[0:6])
print("Saumya Bansal"[-6:])
print("Saumya Bansal"[:6])
print("-----------------------")

#String Case conversion
print("Saumya Bansal".lower())
print("Saumya Bansal".upper())

# String Striping - to remove unnecessary spaces frim start and end of the String
print("-----------------------")
print("                    Saumya Bansal            ".strip())
print("-----------------------")

# replace something in String
print("Saumya Bansal".replace('a','r'))
print("Saumya Bansal".replace('an','r'))
print("-----------------------")

# count number of words in a String
print("Rishabh Bansal".lower().count('b'))
print('-'*23)

# to find something on String
print("Rishabh Bansal".find('Ba'))
print('-'*23)

# some other methods
print("RishabhBansal".isalpha())
print("Rishabh Bansal".isdigit())
print("Rishabh Bansal".isupper())
print("Rishabh Bansal".islower())
print("123".isalpha())
print("123".isdigit())
print("123".islower())
print("123".isupper())
print('-'*23)

# capitalize the String
print("rishabh bansal".capitalize())
print("rishabh bansal".title())
print('-'*23)

# check for start and end 
print("rishabh bansal".startswith('ris'))
print("rishabh bansal".endswith('sal'))
print('-'*23)

# alignment in String 
print("Rish".center(23,'-'))
print("Rish".ljust(23,'-'))
print("Rish".rjust(23,'-'))

x = [1, 23, 'hello', 1]
print(type(x))
# join("ri","cndjk")
# print()

string = "Hello\nWorld\t!"
print(repr(string))                 # Output: 'Hello\nWorld\t!'
print(string)

str1 = '''She said, "I'm learning Python."'''       #with help of triple quotes we can have double and single quotes in String
print (str1)              # Output: She said, "I'm learning Python."
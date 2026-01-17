# ASCII = American Standard Code for Information Exchange
# it starts with Esclamation mark "!" with value = 33
# [0 to 9] ascii value is [48 to 57]
# [A to Z] ascii value is [65 to 90]
# [a to z] ascii value is [97 to 122]

print("A")
print(ord("A"))         # to check the ASCII code 
print(ord('0'))         # ord can only take value as single string character
print(ord(' '))
print("*"*50)

# here we can only perform "ord" operation for one character at a time

# to check what 48 denotes in ASCII we use char function

print(chr(48))          # convet ASCII to actual english character
print("*"*50)

# Python ascii() function returns a string containing a printable representation of an 
# object and escapes the non-ASCII characters in the string using \x, \u or \U escapes. 
# It's a built-in function that takes one argument and returns a string that represents the 
# bject using only ASCII characters

print(ascii("¥"))

s = "G ë ê k s f ? r G ? e k s"
print(ascii(s))

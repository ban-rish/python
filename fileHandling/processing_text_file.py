# if we try to open a file in read mode and if that file is not present we will get I/O error
# fc = open("test.txt",'r')
# txt1 = fc.read()
# fc.close()

fd = open(r"D:\DataAnalysis\Python\git\python\Basic Python\impLibraries.txt",'r')
txt = fd.read()
fd.close()

# here below line tells how many paragraphs are present in the file
para = txt.split("\n\n")
print(type(para))
print(len(para))
# to print each paragraph
for i in para:
    print(i)

# here below line tells how many lines are present in the file
lines = txt.split(".")
print(type(lines))
print(len(lines)-1)
# to print each line
for i in lines:
    print(i)

# here below line tells how many words are present in the file
words = txt.split(" ")
print(type(words))
print(len(words))
# to print each word
for i in words:
    print(i)

txt = txt.replace("\n", " ")  # Replaces all new lines with spaces
print(txt)
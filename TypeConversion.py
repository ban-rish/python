# int conversion
print(int(3))
print(int(3.5))
print(int(True))
print(int('  31  '))
print('----------------------')

#float conversion
print(float(3))
print(float(3.5))
print(float(True))
print(float('56'))
print('----------------------')

#string conversion
print(str(3))
print(str(3.5))
print(str(True))
print(str('jiji'))
print('----------------------')

#Boolean conversion
print(bool(3832))
print(bool(3832.748347))
print(bool(0))
print(bool(0.0000))
print(bool(' '))
print(bool(''))
print(bool('3832'))
print('----------------------')

#two step conversion
print(int(float("3.14")))
print(float(int(.322)))

print(type(type(int)))      #output class<Type>
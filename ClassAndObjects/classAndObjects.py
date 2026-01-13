# A class in Python is a user-defined template for creating objects. 
# It bundles data and functions together, making it easier to manage and use them.

# An object is a specific instance of a class. 
# It holds its own set of data (instance variables) and can invoke methods defined by its class.

# In Python, class has __init__() function which automatically initializes object attributes 
# when an object is created. The __init__() method is the constructor in Python.

class person:
     name = "Rishabh"
     Age = 29
p1 = person()       # creation of Object
p2 = person()
print(p1)           # it tells P1 is an object of class Person
print(p1.name)
print(p1.Age)

p1.Age = 34
p1.name = 'Sam'
print(p1.name)          # here we make changes to P1 Object not the class Variable
print(p1.Age)

print(p2.name)          
print(p2.Age)
print('*'*50)

# methods are the functions defined in the classes

class mathematics:
     name = "rish"

# self parameter is a reference to the current instance of class. 
# It allows us to access the attributes and methods of the object.

     def greeting(self):
         print("Hi there")
         return "HI"
     
     def greet(self):           # when we define any method inside a class, by default there is an argument "self" present in that method arguments
        print("Hello")                        # error we get is - greet() takes 0 positional arguments but 1 was given
        print("hello",self.name)    # to access a class level attribute we need to use "self"
     
     def factorial(self,n):
         s=1
         for i in range (1,n+1):
             s*=i
         return s
     
     def lst_mult(self, lst):
         s = 1         
         for i in lst:
             s*=i
         return s
     
     def lst_dot(self, lst1, lst2):
         return [lst1[i]*lst2[i] for i in range(len(lst1))]

math = mathematics()
math.greet()
print(math.greet())             # as greet method does not return anything, so "print" would return Nothing so it returns NONE as well
print('*'*50)
print(math.greeting())          # here "greeting" is returning something so it does not Print NONE in the end
print('*'*50)
print(math.factorial(5))
print('*'*50)
print(math.lst_mult([1,2,3,4,5]))
print('*'*50)
print(math.lst_dot([1,2,3,4],[5,6,7,8]))

# init method example
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# __str__ method in Python allows us to define a custom string representation of an object.
    def __str__(self):
        return f"{self.name} is {self.age} years old."

dog1 = Dog("Buddy", 3)

print(dog1.name)  
print(dog1.species)
print('*'*50)

# Class Variable are variables that are shared across all instances of a class. 
# It is defined at class level, outside any methods. 
# All objects of class share same value for a class variable unless explicitly overridden.

# Instance Variables are unique to each instance (object) of a class. 
# These are defined within __init__() method or other instance methods. 
# Each object maintains its own copy of instance variables, independent of other objects.

# Getter: Used to access value of an attribute.
# Setter: Used to modify value of an attribute.
# example  of Getter and Setter
class Dog:
    def __init__(self, name, age):
        self._name = name  # Conventionally private variable
        self._age = age  # Conventionally private variable

    @property
    def name(self):
        return self._name  # Getter

    @name.setter
    def name(self, value):
        self._name = value  # Setter

    @property
    def age(self):
        return self._age  # Getter

    @age.setter
    def age(self, value):
        if value < 0:
            print("Age cannot be negative!")
        else:
            self._age = value  # Setter
print('*'*50)

# Method overriding occurs when a subclass provides a specific implementation of a 
# method that is already defined in its superclass. This allows subclasses to modify or 
# extend behavior of inherited methods.
# Method Overriding example  
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):  # Method overriding
        print("Woof")

dog = Dog()
dog.sound()
print('*'*50)

# Static Method: A method that does not require access to instance or class. 
# It’s defined using @staticmethod decorator.
# Class Method: A method that receives the class as its first argument (cls). 
# It’s defined using @classmethod decorator.

class Dog:
    @staticmethod
    def info():
        print("Dogs are loyal animals.")

    @classmethod
    def count(self):
        print("There are many dogs of class", self)

dog = Dog()
dog.info()  # Static method call
dog.count()  # Class method call
print('*'*50)

# Abstract classes provide a template for other classes. 
# These classes can't be instantiated directly. 
# They contain abstract methods, which are methods that must be implemented by subclasses.
# Abstract classes are defined using abc module in Python.

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Woof")

dog = Dog()
dog.sound()
# to create a class use the below syntax

class Dog:
    sound = "bark"



obj1 = Dog()


print(obj1.sound)


print("===========================================================")
#python does not support multiple constructors it can have params with default values

class Person:
    name = ""
    age = ""

    def __init__(self,name="",age=0):
        self.name = name
        self.age = age

    #you pass the self keyword as a referance to the current object
    def bark(self):
        print(f"{self.name} is barking")

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    

obj1 = Person()
obj2 = Person("Ahmed")
obj3 = Person("Ahmed",30)


print(obj1.name,obj1.age)
print(obj2.name,obj2.age)
print(obj3.name,obj3.age)


obj2.bark()

print(obj3)

print("======================================================")

#there are two types of variables defined in the class

# 1- class variables :- that is defined outside of the __init__ function and changing it changes the value for all instances
# 2- instance variables :- that is defined inside the __init__ function and it's value is unique to each instance

class Dog:
    #class variable
    species = "Golden retriver"

    def __init__(self,name,age):
        #instance variable
        self.name = name
        self.age = age


dog1 = Dog("Max",12)
dog2 = Dog("Roy",10)

# Access class and instance variables
print(dog1.species)  # (Class variable)
print(dog1.name)     # (Instance variable)
print(dog2.name)     # (Instance variable)

# Modify instance variables
dog1.name = "Boddy"
print(dog1.name)     # (Updated instance variable)

# Modify class variable
Dog.species = "Feline" #access the class 
print(dog1.species)  # (Updated class variable)
print(dog2.species)


print("===================================================")





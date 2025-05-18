
#this is how you import the module and you can add alise or name to it too

import mymodule as mx


#there are several modules built-in in python
import platform

mx.greetings()

print(mx.person1["name"])
print(mx.person1["age"])
print(mx.person1["country"])

print("==================================================================")


x = platform.system()

print(x)

print("==================================================================")

# the dir function is built-in and is used to list all the names and function that belong to spacific module
print(dir(platform))

print(dir(mx))

print("==================================================================")

from mymodule import greetings

greetings()



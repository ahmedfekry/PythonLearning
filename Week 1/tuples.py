thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


print("==========================================")

#to get the length of a tuple 

print(len(thistuple))

# tuples can have any datatype

thistuple = ("apple",True,123)

print(thistuple)


print("==========================================")


print(type(thistuple))

print("==========================================")

#you can use the tuple constructor to define a tuple

thistuple = tuple(("ahmed","mohamed","fekry"))
print(thistuple)


print("==========================================")

#tuples can be accessed using index

print(thistuple[1])


print("==========================================")

#using negative values means to start from the end

print(thistuple[-1])

print("==========================================")

#you can use the range to get range of values and the return result will be tuple

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[2:5]) # as usual second index will not be included

print(thistuple[:5]) # this means to get from the start untill index 5

print(thistuple[2:]) # this means to get from 2 to the end

print("==========================================")

# to check if the 
if "apple" in thistuple:
    print("Yes 'apple' is included")

print("==========================================")

# to convert a tuple to a list your 
x = ("apple", "banana", "cherry")

y = list(x)

y[1] = "kiwi"

x = tuple(y)

print(x)

print("==========================================")

#to add items to tuple you can change the tuple to a list then add the item and convert it back to tuple
#or you can add tuple to tuple using + operator
#to remove an item from a tuple you need to do the same 

thistuple = ("apple","banana","cherry")

y=("orange",)

thistuple += y

print(thistuple)

print("==========================================")

#to delete the tuple completely you need to use the del key

del thistuple

# print(thistuple) #this should give an error

print("==========================================")

# this is called packing a tuple
fruites = ("orange","apple","kiwi")

#this is called unpacking
(x,y,z) = fruites

print(x)
print(y)
print(z)


print("========================================")

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

#unpacking with asterisk
(a,b,*c) = fruits

print(a)
print(b)
print(c)


print("====================xxx==========================")


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


print("===================xxx===========================")

#looping through the tuple is the same as the list looping


for x in fruits:
    print(x)

print("==========================================")

firsttuple=(1,2,3)

secondtuple=(4,5,6)

thirdtuple = firsttuple + secondtuple

print(thirdtuple)

print("==========================================")

#this can multiply the tuple many times which means repeating it
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

print("==========================================")



print("==========================================")



print("==========================================")



print("==========================================")






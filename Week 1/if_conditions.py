#most important thing about if statements is the indentations

a = 100
b = 200

if a < b:
    print("a is less than b")


#this is the incorrect syntax
"""
a = 100
b = 150

if a < b:
print("sdfsdfsdf ") # this will raise error

"""

if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else:
    print("a is equal to b")


print("================================================")

#short hand syntax
if a > b: print("a is greater than b")

print("================================================")

a = 2
b = 100

print("a") if a < b else print("b")

print("================================================")

#you can use (and) & (or)
a = 10
b = 19
c = 40

if a < b and b < c: 
    print("c is the greatest")

print("================================================")

if not a > b:
    print("Foo")

print("================================================")

#nested is statements
x = 100

if  x > 50:
    print("Even ten")
    if x > 75:
        print("seams that x is so big")
    else:
        print("this is normal x")

print("================================================")

# you can use the pass keyword to path a condition
a = 33
b = 150

if  a > b:
    pass

print("================================================")



print("================================================")



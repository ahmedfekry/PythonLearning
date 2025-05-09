


x,y,z = "Ahmed","Mohamed","Fekry"

print(x)
print(y)
print(z)


x=y=z = "Gooooo"

print(x)
print(y)
print(z)


fruits = ["Apple","Banana","cherry"]

x,y,z = fruits

print(x + y + z)
# print(y)
# print(z)

x = 5
y = "10"
# this gives error
# print(x + y)


# Global variables
print("=============================================================")

c = "Awsome" # this is global outside the function

def function():
    global c # use global keyword for accessing the global variable c 
    c = "Good" # this is local inside the function
    print(c)

function()
    
print(c)
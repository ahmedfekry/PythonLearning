fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print("===========================================")

for x in "banana":
  print(x)

print("===========================================")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
print("=============================================")

#you can use the range function to create array of integers starting from 0 to a value-1
#remember that the value is not included
# also you can use start and end 
#ex. range(2,6)
for x in range(6): 
  print(x)

print("=============================================")


for x in range(2,10):
  print(x)

print("=============================================")

#also you can spacify a step parameter
for x in range(2,10,2):
  print(x)

print("=============================================")

for x in range(6):
  print(x)
else:
  print("Finally finished!")

print("=============================================")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
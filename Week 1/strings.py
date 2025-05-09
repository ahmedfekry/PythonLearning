# '' is the same as ""

print("Hello")
print('Hello')


print("this is ' ")

print('this is \'')

print('this is "')

# string are arrays in python

name = "My name is Ahmed"

print(name[9])

# looping on a string

for x in name:
    print(x)


#get string length

print(len(name))

# search for a word in string
# this is case sensitive
if "Ahmed" in name:
    print("yes")
else:
    print("NO")

print("m" in name)

print("==================")

print("man" not in name)

print("==================")

if  "girl" not in name:
    print("YES")


# Slice string
# from position 2 to 10 (not included)
print(name[2:10])

print(name[:5]) #slice from start to 5

print(name[2:]) #slice from 2 to end

print("==================")

#my name is Ahmed
print(name[-5:-2]) #slice from the end of the string


# Modify strings












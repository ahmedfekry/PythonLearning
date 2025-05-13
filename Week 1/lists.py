mylist = ["apple","banana","orange"]

print(mylist)

print("========================================")

mylist = ["apple","banana","orange","apple","banana"]

print(len(mylist))

print("========================================")

mylist = ["apple",True,3,False,"orange",25]

print(len(mylist))

print("========================================")

print(type(mylist))

print("========================================")

mylist = list(("apple","post",35))

print(mylist)

print("========================================")

print(mylist[1])

print("========================================")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[2:5]) # remember that the second index is not included

print(thislist[-4:-1]) # this will print from orange to melon (will not include the second index)

print("========================================")

thislist = ["apple","banana","cherry"]

thislist[1] = "Kiwi"

print(thislist)

print("========================================")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

thislist[1:4] = [2,3,5] # if you inserted more items than the indexs 

print(thislist)

print("========================================")

thislist = ["apple", "banana", "cherry"]

thislist.insert(2,"Fooo")

print(thislist)

print("========================================")


thislist.append("new fruit")

print(thislist)

print("========================================")

newlist = ["manago","egg"]

thislist.extend(newlist) # this can also be used to add tuble and sets

print(thislist)

print("========================================")

thislist.remove("manago") #removes the first occurance

print(thislist)

print("========================================")

thislist.pop(1) #removes the spacified index if no index then it removes the last item

print(thislist)

print("========================================")


del thislist[0] # can also be used to delete the list completly from the memeory

print(thislist)

print("========================================")

# del thislist

print(thislist)

print("========================================")

thislist.clear() #this empty the list and removes all items from it

print(thislist)

print("========================================")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

for x in thislist:
    print(x + ",")

print("========================================")

for i in range(len(thislist)):
    print(thislist[i])

print("========================================")

i = 0
while i < len(thislist):
    print(thislist[i])
    i+=1

print("========================================")

#short hand syntax to loop through the list is list comprehension

[print(y) for y in thislist]


print("========================================")


#list comprehension

# without list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = []

for x in fruits:
    if 'a' in x:
        newlist.append(x)

print(newlist)

#with list comprehension

newlist = [x for x in fruits if 'a' in x]

print(newlist)

# the syntax is like the below

# newlist = [expression for item in iterable if condition == True]

print("========================================")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

print("========================================")

#Sort the list 

thislist = [19,20,10,2,5,1,50]

thislist.sort()

print(thislist)

print("========================================")

thislist.sort(reverse=True)

print(thislist)

print("========================================")

newlistints = [19,20,10,2,5,1,50]

def myfunc(x):
    return abs(x-50)

31,30,40,48,45,49,0

# thislist = [19,20,10,2,5,1,50]

newlistints.sort(key=myfunc)

print(newlistints)

print("========================================")

#to a list to another, use the copy method

mylist = thislist.copy();

print(mylist)

#or use the built in method list

mylist = list(thislist)

print(mylist)

#or by using the slice operator

mylist = thislist[:]

print(mylist)

print("========================================")

list1 = ["a","b","c"]
list2 = [1,2,3]

# list3 = list1+list2
# print(list3)

# for x in list2:
#     list1.append(x)

# print(list1)

# you can use the extend method
list1.extend(list2)

print(list1)


print("========================================")


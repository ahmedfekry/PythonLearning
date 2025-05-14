#sets are unordered which means that everytime you print the list will be in different order

thisset = {"apple","banana","chery","kiwi"}

print(thisset)

print("==================================================================================")

#sets are unchangeable which means that you can't change the values once created

my_set = {1, 2, 3, "hello", (4, 5)}  # integers, strings, and tuples are immutable

# my_set = {1, 2, [3, 4]}  # ❌ Error: lists are mutable this is what meant by unchangeable because that the list


print("==================================================================================")

#sets doesn't allow duplicates

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)


print("==================================================================================")

# 1 & true is considered the same value
thisset = {"apple", "banana", "cherry", True, 1, 2,False,0}

print(thisset)

print("==================================================================================")

#to get the length of a set use the len function

print(len(thisset))

print("==================================================================================")

myset = {"apple", "banana", "cherry"}
print(type(myset))


print("==================================================================================")

#the set constructor

thisset = set(("apple","banana"))

print(thisset)

print("==================================================================================")

thisset = {"apple","banana","cherry"}

for x in thisset:
    print(x)


print("==================================================================================")

print("banana" in thisset)

print("==================================================================================")

print("kiwi" not in thisset)

print("==================================================================================")

thisset.add("kiwi")

print(thisset)

print("==================================================================================")


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

# the items can by of any collection
thisset.update(tropical)

print(thisset)


print("==================================================================================")

thisset.remove("banana")

print(thisset)

#remove method will raise an error if the item is not found

# thisset.remove("kiwi") #this will raise error because kiwi is not found

print("==================================================================================")


thisset.discard("kiwi") #this will not raise errors

print("==================================================================================")

#you can use the pop method but this method removes a random

x = thisset.pop()

print(x)

print("==================================================================================")

thisset = {"apple","banana","cherry"}

thisset.clear()

print("==================================================================================")

thisset = {"apple","banana","cherry"}

del thisset

# print(thisset) #this will give error

print("==================================================================================")

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2) # you use the pipe | instead of the union keyword

print(set3)

print("==================================================================================")

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)

print(myset)

print("==================================================================================")


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

print("==================================================================================")

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2) #this will get the intersection of the two sets

#you can use the & operator as well

print(set3)

print("==================================================================================")

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)# this will get the items in the first set that doesn't exist in the second set

#you can use the - operator as well

print(set3)

print("==================================================================================")

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2) # this is the same as difference but it will change the original set

print(set1)

print("==================================================================================")

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)# this will merge the two sets but will remove the duplicates
# symmetric_difference_update will update the original set

set1.symmetric_difference_update(set2)

print(set3)


print("==================================================================================")


print("==================================================================================")


print("==================================================================================")


print("==================================================================================")


print("==================================================================================")


print("==================================================================================")
#dictionary is used to store key-value pair, 
# it ordered and unchangable and don't allow duplicates


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year":1994, # this will override the previous one,
  "colors": ["red","green","blue"]
}


print(thisdict)

print(thisdict["brand"])

print(len(thisdict))

print("==========================================================")

thisdict = dict(name="Ahmed",age=30,nationality="Egyptian")

print(thisdict)

print("==========================================================")
#you can access items using the key or the get method

print(thisdict["name"])

print(thisdict.get("age"))

print("==========================================================")
#you can get all keys using keys function

print(thisdict.keys())


print("==========================================================")
#The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

x = thisdict.keys()

print(x)

thisdict["word"] = "Software engineer"

print(x)

print("==========================================================")
#all rules applied to keys are also applicable on values

y = thisdict.values()

print(y)

thisdict["name"] = "Fekry"

print(y)

print("==========================================================")

#items will return all key-value pair as a tuple and it has the same rules as keys and values functions

v = thisdict.items()

print(v)

thisdict["status"] = "Married"

print(v)

print("==========================================================")
#to check if key exists use the if in condition

if "name" in thisdict:
    print("The 'name' key already exists")

print("==========================================================")
#you can use the pop method to remove items form the dictionary

thisdict.pop("word")

print(thisdict)

#or you can use the popitem to remove the laster inserted item

thisdict.popitem()
print(thisdict)

#or you can use the del item and it can also delete the dictionary completely

del thisdict["age"]
print(thisdict)

#the clear method empties the dictionary items

# thisdict.clear()
# print(thisdict)
print("==========================================================")

#to make a copy of dictionary you can't use the assign method dict = dict you need to use copy or dict methods
newdict = thisdict.copy()

print(newdict)

print("==========================================================")
#this is called nested dictionary

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])

print("==========================================================")
#in order to loop through nested dictionary use the below 

for x, obj in myfamily.items():
  print(x)

#   for y in obj:
#     print(y + ':', obj[y])


print("==========================================================")


print("==========================================================")

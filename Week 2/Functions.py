#to define a function you can use this syntax

"""
    no return types and no brackets

"""
def function_name(fname,lname):
    print(f"Hello my name is {fname} {lname}")
    return 0


# just use the function name and params
function_name("Ahmed","Fekry")


print("=====================================================")
#Arbitry arguments, if you don't know the number of arguments use the * before the argument name 
# to idecate the the function expects unknow number of params

def printKids(*args):
    print(f"i have, {args[0]}, {args[1]}, {args[2]}")


printKids("Yazan","Misk","Ali")

print("=====================================================")
#the order of the argument doesn't matter if you use argment name 

def test_func(fname,mname,lname):
    print("{fname} {mname} {lname} ")


test_func(lname="Fekry",mname="Mohamed",fname="Ahmed")

print("=====================================================")
#arbitrary keyword argument is compination between arbitrary and keyword

def new_func(**args):
    print(f"{args['fname']} {args['lname']} {args['mname']}")

new_func(fname="Ahmed",lname="fekry",mname="Mohamed")
print("=====================================================")

#you can pass any datatype, string,numbers,booleans,arrays

def any_func(arg):
    for x in arg:
        print(x)

food = ["apple","banana","cherry"]

any_func(food)


print("=====================================================")

def math(x,y):
    return x*y*2

print(math(10,12))

print("=====================================================")

#positional only arguments

def cunname(x, /):
    print(x)

#keyword only argument
def xunname(*,x):
    print(x)


cunname(100)
xunname(x = 200) #this should throw error


# cunname(x = 100) #this should throw error
# xunname(100)

# Combine Positional-Only and Keyword-Only
# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.



def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

print("=====================================================")



print("=====================================================")



print("=====================================================")



print("=====================================================")



print("=====================================================")

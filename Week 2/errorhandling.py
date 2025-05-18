# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.


try:
    print("Hello world")
    print(z)
    # x = 100/0
except: #this will be excuted in case of exeptions only 
    print("This is the exception block")
else: # this will be excuted when there is any errors
    print("My name is Ahmed")
finally: # this block will be excuted anyway
    print("this is the result")


print("====================================================")

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")


print("====================================================")

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
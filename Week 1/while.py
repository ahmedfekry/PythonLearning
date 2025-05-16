

i=0

while i < 10:
    print(i)
    i += 1

print("====================================")

x = 1

while x < 10:
    print(x)
    if x == 5:
        print("this is enough")
        break #of caurse there is continue keyword
    x+=1

print("====================================")

# you can use the else key word with the while loop to do something when the condition evaluates to false
i = 1
while i < 9:
    print(i)
    i+=1
else:
    print("i has reached the 10")

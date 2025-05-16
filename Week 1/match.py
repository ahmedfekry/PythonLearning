#match in like the switch statement in other languages
""""
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
"""

day = 4

match day:
    case 1:
        print("saturday")
    case 2:
        print("sunday")
    case 3:
        print("monday")
    case 4:
        print("tuesday")
    case 5:
        print("wednesday")
    case 6: 
        print("thursday")
    case 7: 
        print("friday")
    case _: #this is the default condition
        print("There is no day with that number")

print("================================================")

match day:
    case 1 | 2:
        print("weekend")
    case 3 | 4 | 5 | 6 | 7:
        print("weekday")
    case _:
        print("There is no day with that number")
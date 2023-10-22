# Match
# Similar to switch in Java

# Using number

number = int(input("Enter a number: "))

match number:
    case 1:
        print("You have entered 1")
    case 2:
        print("You have entered 2")
    case 3:
        print("You have entered 3")
    case _:
        print("This is default case")

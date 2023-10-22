# Match case

# using string

name = input("Enter name: ")

match name:
    case "rohan":
        print("Your")
        print("name")
        print("is")
        print("Rohan")
    case "rocky":
        print("Your name is Rocky")
    case _:
        print("This is default")

# File IO in Python

# Read

try:
    file = open("dummy2.txt", "r")
except Exception as error:
    print("Error occurred:", error)
else:
    print(file.read())
    file.close()
finally:
    print("This is finally block")

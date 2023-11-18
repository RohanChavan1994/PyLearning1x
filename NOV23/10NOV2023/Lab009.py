# File IO in Python

# Read

file = open("dummy.txt", "r")
print(file.read())
file.close()

# Append

file = open("dummy.txt", "a")
file.write("New line added.")
file.close()

# Read

file = open("dummy.txt", "r")
print(file.read())
file.close()

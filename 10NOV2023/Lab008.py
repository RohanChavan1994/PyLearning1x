# File IO in Python

# Read

file = open("dummy.txt", "r")
print(file.read())
file.close()

# Write

file = open("dummy.txt", "w")
file.write("Same line added.")
file.close()

# Write

file = open("dummy1.txt", "w")
file.write("Same line added in file.")
file.close()
# String functions

# Strings are immutable in nature ->  cannot be changed once created

name = "rohan"

# Address reference of variable
print(id(name))

# Capitalize first character in string
print(name.capitalize())

# Capitalize all the characters in string
print(name.upper())

# All the characters in string are converted to lowercase
print(name.lower())

# Swaps the case of characters
print(name.swapcase())

# Title case -> Capitalize first character of each word in string
text = "hello world"
print(text.title())

# Length
print(len(text))

# Replace
print(text.replace("world", "Python"))

# Count
print(text.count("o"))

# Find
print(text.find("o"))
print(text.rfind("o"))
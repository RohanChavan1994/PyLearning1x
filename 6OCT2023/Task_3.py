# Task 3
# List the all the functions avaiable for the String Data Type.
# e.g len()

# Case changing methods
string = "tHiS tExT iS wRiTtEn In SnAkE cAsE"
print("String used for demonstration:", string)

# lower(): Converts all uppercase characters in a string into lowercase
print("After using lower():", string.lower())

# upper(): Converts all lowercase characters in a string into uppercase
print("After using upper():", string.upper())

# title(): Convert string to title case(first character of each word is capital and remaining characters are lowercase
print("After using title():", string.title())

# swapcase(): Swap the cases of all characters in a string
print("After using swapcase():", string.swapcase())

# capitalize(): Convert the first character of a string to uppercase
print("After using capitalize():", string.capitalize())

# casefold(): The casefold() method in Python converts all the uppercase letters in a string to lowercase letters.
# casefold() is similar to the lower() method, but is stronger and helps with changing letters to lowercase in other languages.
print("After using casefold():", string.casefold())

# islower(): Checks if all characters in the string are lowercase
print("Using islower(), checking if all the characters in string are lowercase :", string.islower())

# isalpha(): Returns “True” if all characters in the string are alphabets
print("Using isalpha(), checking if all the characters in string are alphabets :", string.isalpha())





# Misc methods
# center(): Pad the string with the specified character
print("Using center(), padding string with $ five times on both side:", string.center(len(string) + 10, "$"))

# count(): Returns the number of occurrences of a substring in the string
print("Using count(), finding occurrences of \"t\" starting from fifth index:", string.count("t", 5))

# endswith(): Returns “True” if a string ends with the given suffix
print("Using endswith(), checking if string ends with \"E\":", string.endswith("E"))

# find(): Returns the lowest index of the substring if it is found
print("Using find(), finding lowest index for the occurrence of \"iS\":", string.find("iS"))

# index(): Returns the position of the first occurrence of a substring in a string
print("Using index(), finding index for first occurrence of \"iS\":", string.find("iS"))








# isalnum(): Checks whether all the characters in a given string is alphanumeric or not
print("Using isalnum(), checking if all the characters in string is alphanumeric or not :", string.isalnum())

# isdecimal(): Returns True if all the characters are decimals (0-9)
print("Using isdecimal(), checking if all the characters in string are decimals :", "1234567890".isdecimal())

# isdigit(): Returns “True” if all characters in the string are digits
print("Using isdigit(), checking if all the characters in string are digits :", "1234567890".isdigit())

# isidentifier(): Check whether a string is a valid identifier or not(it only consists of alphanumeric characters and
# underscore and doesn’t start with a space or a number
print("Using isidentifier(), checking if the string is a valid identifier :", "_variable_name_03".isidentifier())

# isnumeric(): Returns “True” if all characters in the string are numeric characters
print("Using isnumeric(), checking if all the characters in string are numeric characters :", string.isnumeric())

# isprintable()	Returns “True” if all characters in the string are printable or the string is empty
# isspace()	Returns “True” if all characters in the string are whitespace characters
# istitle()	Returns “True” if the string is a title cased string
# isupper()	Checks if all characters in the string are uppercase
# join()	Returns a concatenated String
# ljust()	Left aligns the string according to the width specified
# lower()	Converts all uppercase characters in a string into lowercase
# lstrip()	Returns the string with leading characters removed
# maketrans()	 Returns a translation table
# partition()	Splits the string at the first occurrence of the separator
# replace()	Replaces all occurrences of a substring with another substring
# rfind()	Returns the highest index of the substring
# rindex()	Returns the highest index of the substring inside the string
# rjust()	Right aligns the string according to the width specified
# rpartition()	Split the given string into three parts
# rsplit()	Split the string from the right by the specified separator
# rstrip()	Removes trailing characters
# splitlines()	Split the lines at line boundaries
# startswith()	Returns “True” if a string starts with the given prefix
# strip()	Returns the string with both leading and trailing characters
# swapcase()	Converts all uppercase characters to lowercase and vice versa
# title()	Convert string to title case
# translate()	Modify string according to given translation mappings
# upper()	Converts all lowercase characters in a string into uppercase
# zfill()	Returns a copy of the string with ‘0’ characters padded to the left side of the string

# format(): Formats the string for printing it to console
print("Using format(). Hi, my name is {}. I am {} years old. I am learning {} from {}.".format("Rohan", 28, "\"Python\"", "The Testing Academy"))

# format_map()	Formats specified values in a string using a dictionary
# input stored in variable a
a = {'x': 'John', 'y': 'Wick'}
# Use of format_map() function
print("{x}'s last name is {y}".format_map(a))

# expandtabs(): Replaces “\t” symbol in the string with amount of space specified
text = "Sweden\t\tNorway\t\tDenmark"
print("String with tabs:", text)
print("After using expandtabs(), replacing each tab with one space:", text.expandtabs(1))
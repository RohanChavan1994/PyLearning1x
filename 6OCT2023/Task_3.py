# Task 3
# List the all the functions avaiable for the String Data Type.
# e.g len()

# String used for demonstration
string = "tHiS tExT iS wRiTtEn In SnAkE cAsE"
print("String used for demonstration:", string, end="\n\n")

# Methods to find index of substring
print("Methods to find index of substring:")

# find(): Returns the lowest index of the substring if it is found
print("Using find(), finding lowest index for the occurrence of \"iS\":", string.find("iS"))

# rfind(): Returns the highest index of the substring
print("Using rfind(), finding highest index for the occurrence of \"iS\":", string.rfind("iS"))

# index(): Returns the position of the first occurrence of a substring in a string
print("Using index(), finding index for first occurrence of \"iS\":", string.index("iS"))

# rindex(): Returns the highest index of the substring inside the string
print("Using rindex(), finding highest index for occurrence of \"iS\":", string.rindex("iS"), end="\n\n")


# Case related methods
print("Case related methods:")

# lower(): Converts all uppercase characters in a string into lowercase
print("After using lower():", string.lower())

# casefold(): The casefold() method in Python converts all the uppercase letters in a string to lowercase letters.
# casefold() is similar to the lower() method, but is stronger and helps with changing letters to lowercase in other languages.
print("After using casefold():", string.casefold())

# islower(): Checks if all characters in the string are lowercase
print("Using islower(), checking if all the characters in string are lowercase :", string.islower())

# upper(): Converts all lowercase characters in a string into uppercase
print("After using upper():", string.upper())

# isupper(): Checks if all characters in the string are uppercase
print("Using isupper(), checking if all the characters in string are uppercase :", string.isupper())

# title(): Convert string to title case(first character of each word is capital and remaining characters are lowercase
print("After using title():", string.title())

# istitle()	Returns “True” if the string is a title cased string
print("Using istitle(), checking if the string is a title cased string :", string.istitle())

# swapcase(): Swap the cases of all characters in a string
print("After using swapcase():", string.swapcase())

# capitalize(): Convert the first character of a string to uppercase
print("After using capitalize():", string.capitalize(), end="\n\n")


# String identification methods
print("String identification methods:")

# isalpha(): Returns “True” if all characters in the string are alphabets
print("Using isalpha(), checking if all the characters in string are alphabets :", string.isalpha())

# isalnum(): Checks whether all the characters in a given string is alphanumeric or not
print("Using isalnum(), checking if all the characters in string is alphanumeric or not :", string.isalnum())

# isprintable(): Returns “True” if all characters in the string are printable or the string is empty
print("Using isprintable(), checking if all the characters in string are printable :", string.isprintable())

# isspace(): Returns “True” if all characters in the string are whitespace characters
print("Using isspace(), checking if all the characters in string are whitespace characters :", "\t\t".isspace())

# isidentifier(): Check whether a string is a valid identifier or not(it only consists of alphanumeric characters and
# underscore and doesn’t start with a space or a number
print("Using isidentifier(), checking if the string is a valid identifier :", "_variable_name_03".isidentifier(), end="\n\n")


# Number identifying methods
print("Number identifying methods:")

# isdecimal(): Returns True if all the characters are decimals (0-9)
print("Using isdecimal(), checking if all the characters in string are decimals :", "1234567890".isdecimal())

# isdigit(): Returns “True” if all characters in the string are digits
print("Using isdigit(), checking if all the characters in string are digits :", "1234567890".isdigit())

# isnumeric(): Returns “True” if all characters in the string are numeric characters
print("Using isnumeric(), checking if all the characters in string are numeric characters :", "1234567890".isnumeric(), end="\n\n")


# String splitting methods
print("String splitting methods:")

# partition(): Splits the string into 3 parts at the first occurrence of the separator
print("Using partition(), splits the string into 3 parts:", string.partition("iS"))

# rpartition(): Splits the string into 3 parts at the last occurrence of the separator
print("Using rpartition(), splits the string into 3 parts:", string.rpartition("iS"))

# split(): Split the string by the specified separator
name = "r,o,h,a,n"
list1 = name.split(",")
print(f"Using split(), splitting the text \"r,o,h,a,n\" with , seperator", list1)

# join(): Returns a concatenated String
print("Using join(), joining a list with adding $ as a seperator:", "$".join(list1))

# splitlines(): Splits the string at line breaks
string1 = "tHiS\ntExT\niS\nwRiTtEn\nIn\nSnAkE\ncAsE"
print("String used for demonstration:", string1)
print("Using splitlines():",string1.splitlines(True), end="\n\n")


# String trimming methods
print("String trimming methods:")

# strip(): Returns the string with both leading and trailing characters
text = "    4 spaces trailing, 4 spaces leading    "
print(text)
print("Using strip(), remove spaces from both leading and trailing end:", text.strip())

# lstrip(): Returns the string with leading characters removed
print("Using lstrip(), remove spaces from leading end:", text.lstrip())

# rstrip(): Removes trailing characters
print("Using rstrip(), remove spaces from trailing end:", text.rstrip(), end="\n\n")


# Misc methods
print("Misc methods:")

# replace(): Replaces all occurrences of a substring with another substring
print("Using replace(), replace \"iS\" with \"$$\":", string.replace("iS","$$"))

# center(): Pad the string with the specified character
print("Using center(), padding string with $ five times on both side:", string.center(len(string) + 10, "$"))

# ljust(): Left aligns the string according to the width specified
print("Using ljust(), padding five $ to the right of the string:", string.ljust(len(string) + 5, "$"))

# rjust(): Right aligns the string according to the width specified
print("Using rjust(), padding five $ to the left of the string:", string.rjust(len(string) + 5, "$"))

# zfill(): Returns a copy of the string with ‘0’ characters padded to the left side of the string
print("Using zfill(), padding five 0 to the left of the string:", string.zfill(len(string) + 5))

# startswith(): Returns “True” if a string starts with the given prefix
print("Using startswith(), checking if string starts with \"t\":", string.startswith("t"))

# endswith(): Returns “True” if a string ends with the given suffix
print("Using endswith(), checking if string ends with \"E\":", string.endswith("E"))

# count(): Returns the number of occurrences of a substring in the string
print("Using count(), finding occurrences of \"t\" starting from fifth index:", string.count("t", 5))

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
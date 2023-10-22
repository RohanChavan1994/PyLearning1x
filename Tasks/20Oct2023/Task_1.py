"""
Task #1

Palindrome Checker:
Create a function that checks if a given string is a palindrome
(reads the same forwards and backward). 121

Example - pramod
madam - reverse(madam) -> same
Naman -> reverse -> same
Malayalam

Compare String with the Reverse of the string
"""


def is_palindrome(string1):
    if string1 == string1[::-1]:
        print(f"{string1} is palindrome")
    else:
        print(f"{string1} is not palindrome")


str1 = input("Enter a string: ")

is_palindrome(str1)

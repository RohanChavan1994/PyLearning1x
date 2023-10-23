org_str = input("Enter a string: ")

rev_str = lambda: org_str[::-1]

if org_str == rev_str():
    print(f"{org_str} is palindrome")
else:
    print(f"{org_str} is not palindrome")

input_string = input("Enter 5 duplicate numbers with spaces in between: ")
list1 = input_string.split()
print(list1)
print(sorted(set(list1)))
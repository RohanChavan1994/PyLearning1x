"""
Program 3:
Remove duplicate elements from a list.
my_list = [1, 2, 2, 3, 4, 4, 5]
"""

my_list = [1, 2, 2, 3, 4, 4, 5]
print("List with duplicate elements:", my_list)
my_list = list(set(my_list))
print("List with unique elements:", my_list)

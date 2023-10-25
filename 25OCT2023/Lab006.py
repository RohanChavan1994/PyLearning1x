squares_list = [1, 4, 9, 16, 25, 25, 25]
print(squares_list)
squares_list.pop()  # Deletes last element -> one element from right side
print(squares_list)  # Pop will work with index
squares_list.pop(3)  # Index of element to be deleted
print(squares_list)

my_list = [1, 2, 3]

# remove() -> finds and removes first occurrence of an element from list (from left side)
my_list.remove(2)  # remove works with value
print("List after removing 22:", my_list)

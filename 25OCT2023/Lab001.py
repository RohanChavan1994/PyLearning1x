# List -> Collection of items (duplicates are allowed)

my_list = [1, 2, 3]
my_list2 = [1, True, "Rocky", 12.34]

print("Initial list:", my_list)

# Indexing -> finding element using index
print("Element at index 0:", my_list[0])

# Changing an element from list using index
my_list[1] = 20
print("List after changing element at index 1: ", my_list)

# append() -> add element to the end of list
my_list.append(4)
print("List after appending:", my_list)

# extend() -> append list at the end of another list
my_list.extend([5, 6])
print("List after extending:", my_list)

# insert() -> insert element in middle of list, remaining items will be shifted to the right
my_list.insert(1, 22)
print("list after inserting 22 at index 1: ", my_list)

# copy() -> copy a list, references will be different, change to original list will not affect copy of list
my_list_copy = my_list.copy()
print("Original list:", my_list)
print("Copy of list:", my_list_copy)

# clear() -> Empty the list, delete all elements
my_list_copy.clear()
print("List after clear()", my_list_copy)

# print("Element at index 1 of original list", my_list[1])
# print("Element at index 1 of List after clear()", my_list_copy[1])  # This will throw error

# sort()
my_list.sort()
print("Sorted list:", my_list)

# reverse()
my_list.reverse()
print("Reverse list:", my_list)

# length()
length = len(my_list)
print("Length of list", length)

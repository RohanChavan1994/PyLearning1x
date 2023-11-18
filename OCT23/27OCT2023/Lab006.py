# Set{} is immutable -> Duplicates are not displayed

set1 = set()
print(set1)

set2 = set("Rocky")
print(set2)

set3 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(set3)
print(type(set3))

my_list = set([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
print(my_list)

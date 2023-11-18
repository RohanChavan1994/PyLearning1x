my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

val1 = my_dict.pop('a')  # removes and returns the specified element from the dictionary.

print(val1)
print(my_dict)

val2 = my_dict.popitem() # removes the last inserted key-value pair from the dictionary and returns it as a tuple.
print(val2)
print(my_dict)

del my_dict
# print(my_dict)

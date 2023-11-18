# Dict

my_dict = {"a": 1, "b": 2, "c": 3, "a": 4}
print(my_dict)  # If you hve a duplicate key, latest value will be considered

keys = my_dict.keys()
values = my_dict.values()
print(keys)
print(values)


# Get keys and values into a list
keys_list = list(keys)
values_list = list(values)
print(keys_list)
print(values_list)

print(keys_list[0])
print(values_list[2])

# Dict -> key and value

my_dict = {"a": 1, "b": 2, "c": 3, "a": 4}
print(my_dict)
my_dict2 = my_dict.copy()

my_dict.clear()
print(my_dict)

print(my_dict2)

print(my_dict2.items())
set_dict = set(my_dict2.items())
print(set_dict)

set_dict = list(my_dict2.items())
print(set_dict[0][1])

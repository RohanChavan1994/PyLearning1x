my_dict = {"a": 1, "b": 2, "c": 3, "a": 4}

my_dict.pop("c")
print(my_dict)

# How to iterate over the dict

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

for k, v in my_dict.items():
    print(k,"->", v)

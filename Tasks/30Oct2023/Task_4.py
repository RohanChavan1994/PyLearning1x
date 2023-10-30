"""
Program 4:
Remove a key-value pair from the dictionary.
"""

my_dict = {"name": "Rocky", "age": 28, "state": "KA", "pin_code": 560060}
print("Original dictionary:", my_dict)
my_dict.pop("pin_code")
print("Dictionary after popping pin_code:", my_dict)

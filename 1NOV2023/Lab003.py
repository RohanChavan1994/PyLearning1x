fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
min_len = 6


def check_len(words):
    return len(words) >= min_len


fruits_list = list(filter(check_len, fruits))
print(fruits_list)

fruits_list = list(filter(lambda x: len(x) >= min_len, fruits))
print(fruits_list)

fruits_list = list(map(check_len, fruits))
print(fruits_list)

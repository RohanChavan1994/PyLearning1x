numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]


def is_positive(num):
    return num > 0


positive_nums = list(filter(is_positive, numbers))
print(positive_nums)

positive_nums = list(filter(lambda x: x > 0, numbers))
print(positive_nums)

positive_nums = list(map(lambda x: x > 0, numbers))
print(positive_nums)

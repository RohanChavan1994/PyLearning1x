numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(num):
    return num % 2 == 0


even_nums = list(filter(is_even, numbers))
print(even_nums)

even_nums = list(filter(lambda x: x % 2 == 0, numbers))
print(even_nums)

even_nums = list(map(lambda x: x % 2 == 0, numbers))
print(even_nums)

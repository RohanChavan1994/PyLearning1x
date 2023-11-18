# Map and Filters in List

# Map functions -> where we go from one item and apply a function
numbers = [1, 2, 3, 4, 5, 6]

sq = lambda x: x * x
print(sq(5))

print(numbers)

sq_numbers = []
for i in numbers:
    sq_numbers.append(sq(i))

print(sq_numbers)

# Map function

sq_numbers2 = list(map(lambda x: x * x, numbers))
print(sq_numbers2)


def triple(a):
    return a * 3


triple_list = list(map(triple, numbers))
print(triple_list)

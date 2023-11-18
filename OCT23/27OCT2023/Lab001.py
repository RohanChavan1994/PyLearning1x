# List[] is mutable -> It's content can be changed

my_list = [1, 2, 3, 4, 5]
print(type(my_list))
print(my_list)

my_list[1] = 22
print(my_list)
print(my_list + my_list)
print(my_list * 5)
my_list2 = [my_list, my_list]
print(my_list2)
del my_list2
a, b, c = [22, 33, 44]
print(a)
print(b)
print(c)

print(5 in my_list)
print(6 in my_list)

# Tuple() is immutable -> It's content cannot be changed

car = ("Ford", "Tata", "Nissan", "Nissan", 1, 2.2, True, True)
print(type(car))
print(car)
# car[0] = "Honda"
# print(car)

# Convert tuple to list
cars = list(car)
print(cars)

# Convert list to tuple
l1 = [1, 2, 3, 4, 5]
print(l1)
t1 = tuple(l1)
print(t1)

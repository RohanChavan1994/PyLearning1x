# Task 2
# Take a input from a user and print the table
# How to use the print with formatting f
# print(f''), How can print the same?

# n = 2 & print
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20

n = int(input("Enter a integer: "))
print(f"{n} x 1 = {n*1}")
print(f"{n} x 2 = {n*2}")
print(f"{n} x 3 = {n*3}")
print(f"{n} x 4 = {n*4}")
print(f"{n} x 5 = {n*5}")
print(f"{n} x 6 = {n*6}")
print(f"{n} x 7 = {n*7}")
print(f"{n} x 8 = {n*8}")
print(f"{n} x 9 = {n*9}")
print(f"{n} x 10 = {n*10}\n")

# Using for loop

n = int(input("Enter a integer: "))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
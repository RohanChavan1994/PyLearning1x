# 1. Write a Python program to find the largest number in a list.


def max_number(num_list):
    num2 = []

    for x in num_list:
        num2.append(int(x))
    print(f"Largest number in list {num2} is:", max(num2))


num1 = input("Enter a list of numbers with space as separator: ").split(" ")
max_number(num1)

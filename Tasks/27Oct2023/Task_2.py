# 2. Write a Python program to find the smallest number in a list.


def min_number(num_list):
    num2 = []

    for x in num_list:
        num2.append(int(x))
    print(f"Smallest number in list {num2} is:", min(num2))


num1 = input("Enter a list of numbers with space as separator: ").split(" ")
min_number(num1)

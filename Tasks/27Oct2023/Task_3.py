# 3. Write a Python program to sum all numbers in a list.


def sum_number(num_list):
    num2 = []

    for x in num_list:
        num2.append(int(x))
    print(f"Sum of numbers in list {num2} is:", sum(num2))


num1 = input("Enter a list of numbers with space as separator: ").split(" ")
sum_number(num1)

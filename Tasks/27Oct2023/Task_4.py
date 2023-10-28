# 4. Write a Python program to multiply all numbers in a list.


def product_number(num_list):
    num2 = []
    product = 1

    for x in num_list:
        num2.append(int(x))
    for x in num2:
        product *= x

    print(f"Product of numbers in list {num2} is:", product)


num1 = input("Enter a list of numbers with space as separator: ").split(" ")
product_number(num1)

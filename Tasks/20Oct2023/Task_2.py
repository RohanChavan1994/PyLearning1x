"""
Task #2

Sum of Digits: Create a function that calculates the sum of the digits of a positive integer.
n = 12345
sum = 15
n = 123
sum = 6
"""


def get_sum(num):
    sum1 = 0
    while num != 0:
        sum1 = sum1 + (num % 10)
        num = num // 10

    return sum1


n = int(input("Enter a positive integer: "))
print(get_sum(n))

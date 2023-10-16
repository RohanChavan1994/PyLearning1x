# Create a program that takes two numbers as input and prints whether the first number is greater than,
# less than, or equal to the second number.

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

print(f"Both {num1} and {num2} are equal" if num1 == num2 else f"{num1} is greater than {num2}" if num1 > num2 else f"{num1} is less than {num2}")

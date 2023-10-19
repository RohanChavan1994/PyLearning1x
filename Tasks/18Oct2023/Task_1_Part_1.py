"""
Factorial -> 5*4*3*2*1 = 120

Factorial is the product of all positive integers less than or equal to a given positive integer and denoted by
that integer and an exclamation point. Thus, factorial seven is written 7!, meaning 1 × 2 × 3 × 4 × 5 × 6 × 7.
Factorial zero is defined as equal to 1.
"""

num1 = int(input("Enter a number: "))

if num1 < 0:
    print("Please enter a positive integer")
elif num1 == 0 or num1 == 1:
    print(f"Factorial of {num1} is 1")
else:
    factorial = 1
    for x in range(1, num1+1):
        factorial *= x
    print(f"Factorial of {num1} is {factorial}")

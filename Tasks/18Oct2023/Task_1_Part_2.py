"""
# Fibonacci -> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
Fibonacci sequence, the sequence of numbers 1, 1, 2, 3, 5, 8, 13, 21, …, each of which, after the second,
is the sum of the two previous numbers; that is, the nth Fibonacci number Fn = Fn − 1 + Fn − 2.
"""

num = int(input("Enter number of digits to display: "))

# first two numbers
n1, n2 = 0, 1
count = 0

if num <= 0:  # check if the number of digits is valid
    print("Please enter a positive integer")
elif num == 1:  # if there is only one digit, return n1
    print(f"Fibonacci sequence for {num} digit is:", n1)
else:  # generate fibonacci sequence
    print(f"Fibonacci sequence for {num} digits is: ", end="")
    while count < num:
        print(f"{n1}", end=" ")
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1

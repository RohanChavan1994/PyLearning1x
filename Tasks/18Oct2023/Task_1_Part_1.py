# Factorial -> 5*4*3*2*1 = 120

num1 = int(input("Enter a number: "))

if num1 == 0 or 1:
    print(f"Factorial of {num1} is 1")
else:
    factorial = 1
    for x in range(1, num1+1):
        factorial *= x
    print(f"Factorial of {num1} is {factorial}")

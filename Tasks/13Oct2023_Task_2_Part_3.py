# Use the ternary operator to find the maximum of three numbers entered by the user.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

print("All 3 numbers are equal") if num1 == num2 == num3 \
    else print(f"Maximum of {num1}, {num2}, {num3} is:", num1 if num1 > num2 and num1 > num3
    else num2 if num2 > num3 else num3)

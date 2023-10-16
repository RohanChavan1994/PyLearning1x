# Develop a Python script that calculates the square and cube of a given number.

num1 = float(input("Enter a number: "))
print(f"Square of {num1} is:", num1 ** 2)
print(f"Cube of {num1} is:", num1 ** 3)

print(f"Square of {num1} using multiplication is:", num1 * num1)
print(f"Cube of {num1} using multiplication is:", num1 * num1 * num1)

print(f"Square of {num1} using pow() is:", pow(num1, 2))
print(f"Cube of {num1} using pow() is:", pow(num1, 3))

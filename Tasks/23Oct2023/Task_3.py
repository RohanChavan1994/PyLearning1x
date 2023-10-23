# ✅ Create a Function with a Parameter which can do x^y

def power_func(a, b):
    return a ** b


x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))

print(f"{x}^{y} is:", power_func(x, y))

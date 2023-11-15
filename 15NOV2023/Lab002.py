try:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    num3 = num1 / num2
except Exception as error:
    print("Error occurred:", error)
else:
    print(f"{num1}/{num2} =", num3)
finally:
    print("This is finally block.")

a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))

try:
    c = a / b
except Exception as error:
    print("Error occurred:", error)
else:
    print(c)
finally:
    print("This finally block")

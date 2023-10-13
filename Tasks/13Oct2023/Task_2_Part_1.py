# Write a Python program to calculate the area of a circle given its radius using the formula
# area=π×r^2 (Take pie as 3.14)
import math

radius = int(input("Enter the radius: "))
pi = 3.14
area = pi * (radius ** 2)
print("Area of circle is:", area)

area = math.pi * pow(radius, 2)
print("Area of circle using math library is:", round(area, 2))

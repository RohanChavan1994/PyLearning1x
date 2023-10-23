"""
Task 2
✅ Right Triangle Star Pattern

*
**
***
****
*****
"""


def print_triangle(a):
    for i in range(a + 1):
        for j in range(i):
            print("*", end="")
        print(end="\n")


x = int(input('Enter number of levels: '))
print_triangle(x)

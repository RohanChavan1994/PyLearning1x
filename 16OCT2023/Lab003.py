# Max of 3 numbers

x = 5
y = 15
z = 5

if x == y == z:
    print("All 3 numbers are equal")
else:
    output = None
    if x > y and x > z:
        output = x
    elif y > z:
        output = y
    else:
        output = z
    print(f"Maximum of {x}, {y}, {z} is:", output)

print("Using max():", max(x, y, z))

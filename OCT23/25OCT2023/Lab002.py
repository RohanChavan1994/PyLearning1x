squares = [1, 4, 9, 16, 25]

l = squares
l2 = squares.copy()

print(squares)
print(l)
print(l2)

squares.append(36)

print(squares)
print(l)  # If original list changes assigned list also changes
print(l2)  # copy of list is not affected by changes done to the original list

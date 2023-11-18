t1 = ()
t2 = (1, 2, 3, 4, 5)
t3 = tuple(["Rohan", "Rocky", ["Rohan", ["Rohan", "Rocky"], "Rocky"]])
print(t1)
print(t2)
print(t3)

print(t3[2][1][0])  # Indexing
print(min(t2))  # Minimum
print(max(t2))  # Maximum
print(t2.index(5))  # Find index of element
print(t3.count("Rocky"))  # Find how many times the element is present in the tuple

print(t2 + t3)  # Concatenation -> Merging tuples

print(t2 * 3)  # Replication

del t2
print(type(t2))
print(t2)

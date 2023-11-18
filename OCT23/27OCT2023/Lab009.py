set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
print(set2.issubset(set1))
print(set1.issuperset(set2))

set3 = {1, 2, 3, 4, 5}
set4 = {6, 7, 8}
print(set4.isdisjoint(set3))
print(set3.isdisjoint(set4))

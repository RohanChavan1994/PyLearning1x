from collections import Counter

cnt = Counter()
list1 = ["red", "green", "blue", "red", "green", "blue", "red", "green"]

for word in list1:
    cnt[word] += 1

print(cnt)

from collections import Counter

cnt = Counter()
for word in ["red", "green", "blue", "red", "green", "blue","red", "green", "blue"]:
    cnt[word] += 1

print(cnt)

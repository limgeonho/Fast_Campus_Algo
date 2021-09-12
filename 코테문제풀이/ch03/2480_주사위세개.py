# 주사위 세개
from collections import Counter

array = list(map(int, input().split()))

counter = Counter(array)

tmp = counter.most_common(1)[0][1]

for key, value in counter.items():
    if value == tmp:
        if tmp == 1:
            print(max(array)*100)
            break
        elif tmp == 2:
            print(key * 100 + 1000)
            break
        else:
            print(key * 1000 + 10000)
            break
# 블랙잭

from itertools import combinations

n, m = map(int, input().split())

array = list(map(int, input().split()))

answer = []

for i in combinations(array, 3):
    answer.append(sum(i))

answer.sort()

for i in range(len(answer)):
    if answer[i] <= m:
        tmp = answer[i]

print(tmp)
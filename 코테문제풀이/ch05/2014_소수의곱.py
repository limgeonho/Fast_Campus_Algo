# 소수의 곱
# 힙 구조

import heapq
import copy

k, n = map(int, input().split())

array = list(map(int, input().split()))

answer = copy.deepcopy(array)

check = set()

heapq.heapify(answer)

cnt = 0

while cnt < n:
    num = heapq.heappop(answer)
    if num in check:
        continue
    cnt += 1
    check.add(num)
    for i in array:
        heapq.heappush(answer, num*i)
print(num)
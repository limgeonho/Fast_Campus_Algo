# 컵라면
# 그리디는 정렬과 연관이 깊음 => 힙큐 활용!!도 고려하기

import heapq

n = int(input())
array = []
for _ in range(n):
    d, c = map(int, input().split())
    array.append((c, d))

array.sort(key=lambda x: x[1])
heap = []
for arr in array:
    heapq.heappush(heap, arr)
    if len(heap) > arr[1]:
        heapq.heappop(heap)

sum = 0
for a in heap:
    sum += a[0]
print(sum)

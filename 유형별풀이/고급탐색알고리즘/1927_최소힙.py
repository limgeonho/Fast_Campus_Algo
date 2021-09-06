# 최소 힙
import heapq

# n = int(input())
# q = []
#
# for _ in range(n):
#     a = int(input())
#     if a == 0:
#         if q:
#             print(heapq.heappop(q))
#         else:
#             print(0)
#     else:
#         heapq.heappush(q, a)


n = int(input())
heap = []
result = []

for _ in range(n):
    data = int(input())
    if data == 0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap, data)

for data in result:
    print(data)
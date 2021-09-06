# 카드정렬하기
import heapq

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

heapq.heapify(array)

answer = 0
while array:
    if len(array) == 1:
        print(answer)
        break
    tmp_1 = heapq.heappop(array)
    tmp_2 = heapq.heappop(array)
    tmp = tmp_1 + tmp_2
    answer += tmp
    heapq.heappush(array, tmp)

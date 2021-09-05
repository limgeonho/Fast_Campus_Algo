# 좌표 정렬하기

n = int(input())

array = []

for _ in range(n):
    x, y = map(int, input().split())
    array.append([x, y])

array.sort(key=lambda x:(x[0], x[1]))

for arr in array:
    print(*arr)
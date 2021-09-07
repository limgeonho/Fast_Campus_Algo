# 회의실배정
n = int(input())
array = []
for _ in range(n):
    s, e = map(int, input().split())
    array.append((s, e))

array.sort(key=lambda x:(x[1], x[0]))

cnt = 1

tmp = array[0][1]

for i in range(1, len(array)):
    if tmp <= array[i][0]:
        tmp = array[i][1]
        cnt += 1

print(cnt)


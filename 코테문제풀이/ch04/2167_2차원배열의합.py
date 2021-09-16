# 2차원 배열의 합

n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

k = int(input())

for _ in range(k):
    answer = 0
    a, b, c, d = map(int, input().split())
    for i in range(a-1, c):
        for j in range(b-1, d):
            answer += array[i][j]
    print(answer)
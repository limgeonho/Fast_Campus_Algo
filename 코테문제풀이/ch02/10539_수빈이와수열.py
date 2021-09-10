# 수빈이와 수열

n = int(input())

array = list(map(int, input().split()))
answer = []
answer.append(array[0])
for i in range(1, n):
    tmp = 0
    for j in range(i):
        tmp += answer[j]

    answer.append(array[i]*(i+1) - tmp)
print(*answer)
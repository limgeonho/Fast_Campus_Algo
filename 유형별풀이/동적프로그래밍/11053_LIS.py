# LIS
from bisect import bisect_left

# 1번째 방법
n = int(input())
array = list(map(int, input().split()))

answer = []

answer.append(array[0])
for i in range(1, n):
    if answer[-1] < array[i]:
        answer.append(array[i])
    else:
        answer[bisect_left(answer, array[i])] = array[i]

print(len(answer))
print(answer)


# 2번째 방법
n = int(input())
array = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

result = max(dp)
print(result)
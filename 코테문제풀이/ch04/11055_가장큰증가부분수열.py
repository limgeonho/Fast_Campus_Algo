# 가장 큰 증가 부분 수열

import copy
n = int(input())
array = list(map(int, input().split()))

# dp[i] : i 까지 왔을 때, 합의 최대
# dp = copy.deepcopy(array)
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if array[j] < array[i]:
            # dp[i] = max(dp[i], dp[j] + array[i])
            dp[i] = max(dp[i], dp[j] + 1)

print(dp)
print(max(dp))
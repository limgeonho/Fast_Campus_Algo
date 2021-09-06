# 피보나치수

n = int(input())

dp = [0] * 50
dp[0] = 0
dp[1] = 1

for i in range(2, n+2):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])

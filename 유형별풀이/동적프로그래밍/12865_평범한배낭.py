# 평범한배낭
# 냅색알고리즘 -> 반드시 기억할 것

# 1번째 방법
n, k = map(int, input().split())
limited = [0] * (k+1)

for _ in range(n):
    w, v = map(int, input().split())
    for i in range(k, w-1, -1):
        limited[i] = max(limited[i], limited[i-w]+v)

print(limited[k])


# 2번째 방법
n, k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    weight, value = map(int, input().split())
    for j in range(1, k+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)
print(dp[n][k])
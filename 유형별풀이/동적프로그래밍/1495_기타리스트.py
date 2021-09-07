# 기타리스트
# dp문제는 항상 이전의 것을 다음의 것에 활용한다 => 따라서, 매번 뭔가 새로운 정보를 기록해나가면서 누적시키는 것
n, s, m = map(int, input().split())

array = list(map(int, input().split()))

dp = [[0] * (m+1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(1, n+1):
    for j in range(m+1):
        if dp[i-1][j] == 0:
            continue
        if j - array[i-1] >= 0:
            dp[i][j - array[i-1]] = 1
        if j + array[i-1] <= m:
            dp[i][j + array[i-1]] = 1
result = -1
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        result = i
        break
print(result)
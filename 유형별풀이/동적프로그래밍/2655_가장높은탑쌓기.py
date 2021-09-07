# 가장 높은 탑 쌓기(난이도 상!!!ㅋㅋㅋ)
# LIS + 다이나믹프로그래밍
n = int(input())
bricks = []
bricks.append((0, 0, 0, 0))
for i in range(1, n+1):
    a, b, c = map(int, input().split())
    bricks.append((i, a, b, c))

bricks.sort(key=lambda x:x[3])

dp = [0] * (n+1)

for i in range(1, n+1):
    for j in range(i):
        if bricks[i][1] > bricks[j][1]:
            dp[i] = max(dp[i], dp[j] + bricks[i][2])

max_value = max(dp)
index = n
result = []

while index != 0:
    if max_value == dp[index]:
        result.append(bricks[index][0])
        max_value -= bricks[index][2]
    index -= 1

result.reverse()
print(len(result))
for num in result:
    print(num)
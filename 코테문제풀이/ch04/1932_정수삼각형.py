# 정수삼각형
# 주어진 리스트와 같은 모양의 dp리스트를 만들고 계산한 후 값을 작성해나감 -> 이때 dp에 새롭게 작성되는 내용은 이전에 작성된 내용을 활용함
# 삼각형 모양이지만 n*n형태로 맞추고 비어있는 값은 0으로 초기화

n = int(input())

array = [[0 for _ in range(n+1)] for _ in range(n+1)]

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

# tmp에 한 줄 씩 입력받으면서 배열 형성 n*n(삼각형이지만 n*n형태로)
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    for j in range(1, i+1):
        array[i][j] = tmp[j-1]

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + array[i][j]

print(max(dp[-1]))
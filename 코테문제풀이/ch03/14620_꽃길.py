# 꽃길
# 시간복잡도를 확인하고 전수조사를 하는 것도 하나의 방법이다.
# 리스트의 좌표를 확인하는데 있어서
# (x, y) = (flower // n, flower % n) -> 같은 방법도 존재한다..!!!!


#
dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]


def check(lst):
    res = 0
    tmp = []
    for flower in lst:
        x = flower // n
        y = flower % n
        if x == 0 or x == n-1 or y == 0 or y == n-1:
            return 10000

        for w in range(5):
            tmp.append((x + dx[w], y + dy[w]))
            res += array[x + dx[w]][y + dy[w]]
    if len(set(tmp)) != 15:
        return 10000
    return res


n = int(input())
array = []
cost = 10000

for i in range(n):
    array.append(list(map(int, input().split())))

for i in range(n*n):
    for j in range(i+1, n*n):
        for k in range(j+1, n*n):
            cost = min(cost, check([i, j, k]))
print(cost)
# mooyomooyo
# 어려운 dfs 문제...어려워어

def new_check(n):
    return [[False for i in range(10)] for _ in range(n)]


n, k = map(int, input().split())

array = [list(input()) for _ in range(n)]

check_1 = new_check(n)
check_2 = new_check(n)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs_1(x, y):
    check_1[x][y] = True
    cnt = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= 10:
            continue
        if check_1[nx][ny] or array[x][y] != array[nx][ny]:
            continue
        cnt += dfs_1(nx, ny)
    return cnt


def dfs_2(x, y, value):
    check_2[x][y] = True
    array[x][y] = '0'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= 10:
            continue
        if check_2[nx][ny] or array[nx][ny] != value:
            continue
        dfs_2(nx, ny, value)


def down():
    for i in range(10):
        tmp = []
        for j in range(n):
            if array[j][i] != '0':
                tmp.append(array[j][i])
        for j in range(n - len(tmp)):
            array[j][i] = '0'
        for j in range(n - len(tmp), n):
            array[j][i] = tmp[j - (n - len(tmp))]



while True:
    flag = False
    check_1 = new_check(n)
    check_2 = new_check(n)
    for i in range(n):
        for j in range(10):
            if array[i][j] == '0' or check_1[i][j]:
                continue
            res = dfs_1(i, j)
            if res >= k:
                dfs_2(i, j, array[i][j])
                flag = True
    if not flag:
        break
    down()

for row in array:
    print(''.join(row))


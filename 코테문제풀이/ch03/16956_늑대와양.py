# 늑대와 양

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

r, c = map(int, input().split())

array = []
check = False
for _ in range(r):
    array.append(input())

for i in range(r):
    for j in range(c):
        if array[i][j] == 'W':
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < r and 0 <= nj < c and array[ni][nj] == 'S':
                    check = True
                    break

if check:
    print(0)
else:
    print(1)
    for i in range(r):
        print(array[i].replace('.', 'D'))
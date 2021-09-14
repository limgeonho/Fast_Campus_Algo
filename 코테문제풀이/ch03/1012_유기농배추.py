# 유기농배추
# floodfill의 대표적인 문제

from collections import deque

dx = [-1, 0, 1 , 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    global cnt
    cnt += 1
    q = []
    q.append((x, y))

    array[x][y] = 0
    while q:
        now = q.pop(0)
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < M and array[nx][ny] == 1:

                array[nx][ny] = 0
                q.append((nx, ny))


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    array = [[0]*M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        array[b][a] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if array[i][j] == 1:
                bfs(i, j)
    print(cnt)
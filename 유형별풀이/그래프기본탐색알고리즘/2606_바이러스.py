# 바이러스


def bfs(x):
    global cnt
    visited[x] = True
    q = [x]
    while q:
        now = q.pop(0)
        visited[now] = True
        for i in computers[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1

n = int(input())

computers = [[] for _ in range(n+1)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a)

cnt = 0
visited = [False] * (n+1)
bfs(1)
print(cnt)
# 효율적인해킹
from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    visited = [False] * (N+1)
    visited[x] = True
    cnt = 1
    while q:
        now = q.popleft()
        for i in computers[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1
    return cnt


N, M = map(int, input().split())
computers = [[] for _ in range(N+1)]
answer = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    computers[b].append(a)

for i in range(1, N+1):
    tmp = 0
    tmp = bfs(i)

    answer[i] = tmp
print(answer)
max_num = max(answer)

for i in range(1, N+1):
    if answer[i] == max_num:
        print(i, end=' ')
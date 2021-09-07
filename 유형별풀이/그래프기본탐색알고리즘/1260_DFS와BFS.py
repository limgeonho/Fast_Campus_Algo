# DFS와 BFS
# 양방향 그래프인지 꼭 좀 확인하자...ㅂㄷㅂㄷ
def dfs(x):
    result_dfs.append(x)
    visited_dfs[x] = True
    for i in array[x]:
        if not visited_dfs[i]:
            dfs(i)


def bfs(x):
    q = []
    q.append(x)
    visited_bfs[x] = True
    while q:
        now = q.pop(0)
        result_bfs.append(now)
        for i in array[now]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                q.append(i)


n, m, s = map(int, input().split())
array = [[] for _ in range(n+1)]
result_dfs = []
result_bfs = []
for _ in range(m):
    a, b = map(int, input().split())
    array[a].append(b)
    array[b].append(a)

for arr in array:
    arr.sort()

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)
dfs(s)
print(*result_dfs)
bfs(s)
print(*result_bfs)
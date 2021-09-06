# 중량제한

from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]


def bfs(c):
    queue = deque([start_node])
    visited = [False] * (n + 1)
    visited[start_node] = True
    while queue:
        x = queue.popleft()
        for y, weight in adj[x]:
            if not visited[y] and weight >= c:
                visited[y] = True
                queue.append(y)
    return visited[end_node]

start = 100000000000000
end = 1

for _ in range(m):
    x, y, weight = map(int, input().split())
    adj[x].append((y, weight))
    adj[y].append((x, weight))
    start = min(start, weight)
    end = max(end, weight)

start_node, end_node = map(int, input().split())
result = start
while (start <= end):
    mid = (start + end) // 2  # mid 는 현재의 중량을 의미
    if bfs(mid):  # 이동이 가능하므로 중량을 증가시킵니다.
        result = mid
        start = mid + 1
    else:  # 이동이 불가능하므로 중량을 감소시킵니다.
        end = mid - 1
print(result)

# ==================================================================================

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
parent = [i for i in range(N+1)]
graph = []

for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((C, A, B))

# 공장 입력 받기
x, y = map(int, input().split())

# 다리가 들 수 있는 중량이 큰 것부터 내림차순으로 정렬
graph.sort(key=lambda i: i[0], reverse=True)

for cost, a, b in graph:
    # 다리 연결
    union_parent(parent, a, b)
    # 두 공장이 연결 되었을 때
    if find_parent(parent, x) == find_parent(parent, y):
        # 현재 중량 출력
        print(cost)
        break
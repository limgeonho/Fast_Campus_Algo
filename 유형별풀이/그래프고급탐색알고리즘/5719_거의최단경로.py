# 거의최단경로

from collections import deque
import heapq
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(d)
    while q:
        now = q.popleft()
        if now == s:
            continue
        for prev, cost in reverse_array[now]:
            if distance[now] == distance[prev] + cost:
                dropped[prev][now] = True
                q.append(prev)

def dijkstra():
    heap = []
    heapq.heappush(heap, (0, s))
    distance[s] = 0
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for i in array[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost and not dropped[now][i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    s, d = map(int, input().split())

    array = [[]for _ in range(n+1)]
    reverse_array = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, p = map(int, input().split())
        array[u].append((v, p))
        reverse_array[v].append((u, p))

    dropped = [[False]*(n+1) for _ in range(n+1)]

    distance = [1e9] * (n+1)
    dijkstra()

    bfs()

    distance = [1e9] * (n + 1)
    dijkstra()

    if distance[d] != 1e9:
        print(distance[d])
    else:
        print(-1)
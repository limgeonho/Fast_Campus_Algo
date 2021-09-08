# 해킹
# 다익스트라문제임
import heapq

def dijkstra(x):
    q = []
    heapq.heappush(q, (0, x))
    distance[x] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in computers[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())

    computers = [[]for _ in range(n+1)]

    for _ in range(d):
        a, b, s = map(int, input().split())
        computers[b].append((a, s))

    INF = int(1e9)
    distance = [INF] * (n+1)
    dijkstra(c)

    answer = []

    for num in distance:
        if num != INF:
            answer.append(num)
    print(len(answer), end=' ')
    print(max(answer))

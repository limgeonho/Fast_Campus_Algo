# 문제집
# 위상정렬 + 힙큐
import heapq

n, m = map(int, input().split())
indegree = [0]*(n+1)
problems = [[]for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    problems[a].append(b)
    indegree[b] += 1

q = []
result = []
for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

while q:
    now = heapq.heappop(q)
    result.append(now)
    for i in problems[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(q, i)

for num in result:
    print(num, end=' ')
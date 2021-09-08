# 우주신과의 교감
# 크루스칼 알고리즘
import math

def get_distance(p1, p2):
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]
    return math.sqrt((a*a) + (b*b))

def get_parent(parent, n):
    if parent[n] != n:
        parent[n] = get_parent(parent, parent[n])
    return parent[n]

def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())


parent = {}
edges = []
location = []

for _ in range(n):
    x, y = map(int, input().split())
    location.append((x, y))

length = len(location)

for i in range(length-1):
    for j in range(i+1, length):
        edges.append((i+1, j+1, get_distance(location[i], location[j])))

for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

edges.sort(key=lambda x:x[2])

result = 0

for a, b, cost in edges:
    if get_parent(parent, a) != get_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(f'{result:.2f}')
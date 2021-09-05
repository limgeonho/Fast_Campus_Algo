# 친구 네트워크
# 합집합 찾는 union_find 알고리즘

def find(x):
    # if x == parent[x]:
    #     return x
    # else:
    #     parent[x] = find(parent[x])
    #     return parent[x]
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]

T = int(input())

for _ in range(T):
    parent = dict()
    number = dict()

    f = int(input())

    for _ in range(f):
        x, y = input().split()

        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1

        union(x, y)
        print(number[find(x)])

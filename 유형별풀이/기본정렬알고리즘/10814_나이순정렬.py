# 나이순정렬
# 파이썬의 정렬의 기본 값 => 나이순으로 array.sort(key=lambda x:int(x[0])) 정렬하면 나머지는 그냥 원래 있던 순서대로 정렬된다(stable)

n = int(input())

array = []
for _ in range(n):
    age, name = map(str, input().split())
    array.append([age, name])

array.sort(key=lambda x:int(x[0]))

for arr in array:
    print(*arr)
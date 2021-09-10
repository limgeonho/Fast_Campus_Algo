# 수찾기

n = int(input())
array_1 = list(map(int, input().split()))
m = int(input())
array_2 = list(map(int, input().split()))

for num in array_2:
    if num in array_1:
        print(1)
    else:
        print(0)
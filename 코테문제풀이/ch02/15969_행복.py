# 행복

n = int(input())
array = list(map(int, input().split()))

array.sort()

print(array[-1] - array[0])
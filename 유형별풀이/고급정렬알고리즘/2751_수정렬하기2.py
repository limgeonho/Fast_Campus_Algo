# 수 정렬하기2

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

for num in array:
    print(num)
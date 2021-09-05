# 수 정렬하기3
# 받아야하는 값이 많다면 sys.stdin.readline()을 이용하자!!!
import sys
n = int(input())
array = [0] * 10001

for _ in range(n):
    tmp = int(sys.stdin.readline())
    array[tmp] += 1

for i in range(len(array)):
    if array[i]:
        for _ in range(array[i]):
            print(i)
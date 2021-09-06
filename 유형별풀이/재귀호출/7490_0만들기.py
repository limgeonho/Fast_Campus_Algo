# 0 만들기
# 재귀로 연습...
from itertools import product
T = int(input())
for _ in range(T):
    n = int(input())
    array = list(product(['+', '-', ' '], repeat=n-1))
    nums = list(range(1, n+1))
    array.sort()
    for arr in array:
        possible = ''
        for i in range(n-1):
            possible += str(nums[i]) + arr[i]
        possible += str(nums[-1])
        if eval(possible.replace(' ', '')) == 0:
            print(possible)
    print()
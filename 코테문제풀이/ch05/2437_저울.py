# 저울

n = int(input())

array = list(map(int, input().split()))

array.sort()

answer = 0
for num in array:
    if num <= answer+1:
        answer += num
    else:
        break
print(answer+1)
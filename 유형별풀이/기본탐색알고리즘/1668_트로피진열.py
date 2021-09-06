# 트로피진열


def ascend(array):
    res = 1
    tmp = array[0]
    for i in range(1, n):
        if tmp < array[i]:
            tmp = array[i]
            res += 1
    return res


n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

print(ascend(array))

array = array[::-1]

print(ascend(array))
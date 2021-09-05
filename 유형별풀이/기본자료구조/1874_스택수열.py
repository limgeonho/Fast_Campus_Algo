# 스택 수열
n = int(input())
array = []
stack = []
cnt = 1

for i in range(1, n+1):
    data = int(input())
    while cnt <= data:
        stack.append(cnt)
        cnt += 1
        array.append('+')
    if data == stack[-1]:
        stack.pop()
        array.append('-')
    else:
        print('NO')
        exit(0)
print('\n'.join(array))

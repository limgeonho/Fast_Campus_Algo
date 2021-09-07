# 숨바꼭질

n, k = map(int, input().split())

array = [0] * 100001
q = [n]
while q:
    now = q.pop(0)
    if now == k:
        break
    for i in (now+1, now-1, 2*now):
        if 0 <= i < 100001 and not array[i]:
            array[i] = array[now] + 1
            q.append(i)

print(array[k])
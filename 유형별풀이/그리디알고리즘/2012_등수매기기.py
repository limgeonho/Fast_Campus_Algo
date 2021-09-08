# 등수 매기기
# 그리디는 정렬과 연관이 많음...

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

tmp = list(range(1, n+1))
array.sort()
answer = 0
for i in range(n):
    if array[i] != tmp[i]:
        answer += abs(array[i] - tmp[i])
print(answer)

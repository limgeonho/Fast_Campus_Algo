# APC는 왜

n, l, k = map(int, input().split())
questions = []

for _ in range(n):
    easy, hard = map(int, input().split())
    questions.append((easy, hard))
questions.sort(key=lambda x:(x[1], x[0]))

answer = 0
cnt = 0
for i in questions:
    if i[1] <= l:
        answer += 140
        cnt += 1
        if cnt == k:
            break
    else:
        if i[0] <= l:
            answer += 100
            cnt += 1
            if cnt == k:
                break
        else:
            continue
print(answer)
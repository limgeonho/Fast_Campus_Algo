# APC는 왜

# n, l, k = map(int, input().split())
# questions = []
#
# for _ in range(n):
#     easy, hard = map(int, input().split())
#     questions.append((easy, hard))
# questions.sort(key=lambda x:(x[1], x[0]))
#
# answer = 0
# cnt = 0
# for i in questions:
#     if i[1] <= l:
#         answer += 140
#         cnt += 1
#         if cnt == k:
#             break
#     else:
#         if i[0] <= l:
#             answer += 100
#             cnt += 1
#             if cnt == k:
#                 break
#         else:
#             continue
# print(answer)

n, l, k = map(int, input().split())

easy, hard = 0, 0
for i in range(n):
    sub1, sub2 = map(int, input().split())
    if sub2 <= l:
        hard += 1
    elif sub1 <= l:
        easy += 1

answer = min(hard, k) * 140

if hard < k:
    answer += min(k-hard, easy) * 100

print(answer)
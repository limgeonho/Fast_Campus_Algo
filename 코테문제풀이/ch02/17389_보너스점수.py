# 보너스 점수
# 인덱스와 값을 동시에 접근하는 경우에는 enumerate를 생각하자!
n = int(input())
result = input()

bonus = 0
answer = 0

if result[0] == 'O':
    bonus = 0
    answer = 1
else:
    bonus = 0
    answer = 0

for i in range(1, len(result)):
    if result[i] == 'O':
        if result[i-1] == 'X':
            bonus = 0
        else:
            bonus += 1
        answer += ((i+1) + bonus)

print(answer)

# n = int(input())
#
# result = input()
#
# answer = 0
# bonus = 0
# for idx, value in enumerate(result):
#     if value == 'O':
#         answer, bonus = answer + (idx+1) + bonus, bonus+1
#     else:
#         bonus = 0
# print(answer)
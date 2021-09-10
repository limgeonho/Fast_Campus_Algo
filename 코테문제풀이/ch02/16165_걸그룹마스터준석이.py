# 걸그룹 마스터 준석이

n, m = map(int, input().split())
group_1 = {}
group_2 = {}
for _ in range(n):
    name = input()
    number = int(input())
    tmp = []
    for _ in range(number):
        member = input()
        tmp.append(member)
        group_2[member] = name
    tmp.sort()
    group_1[name] = tmp
question = []
for _ in range(m):
    quiz = input()
    quiz_type = int(input())
    question.append((quiz_type, quiz))

for i in question:
    if i[0] == 1:
        print(group_2[i[1]])
    else:
        for j in group_1[i[1]]:
            print(j)
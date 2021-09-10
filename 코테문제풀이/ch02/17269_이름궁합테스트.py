# 이름궁합테스트

numbers = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 4,
           'F': 3, 'G': 1, 'H': 3, 'I': 1, 'J': 1,
           'K': 3, 'L': 1, 'M': 3, 'N': 2, 'O': 1,
           'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2,
           'U': 1, 'V': 1, 'W': 1, 'X': 2, 'Y': 2,
           'Z': 1}

n, m = map(int, input().split())
name1, name2 = map(str, input().split())

change = []

name1 = list(name1)
name2 = list(name2)

while True:
    if len(name1) == 0:
        change.extend(name2)
        break
    elif len(name2) == 0:
        change.extend(name1)
        break
    else:
        change.append(name1.pop(0))
        change.append(name2.pop(0))

answer = []
for alpha in change:
    answer.append(numbers[alpha])

for i in range(n + m - 2):
    for j in range(n + m - 1 - i):
        answer[j] += answer[j+1]

num1 = answer[0] % 10 * 10
num2 = answer[1] % 10

print(str(num1+num2) + '%')
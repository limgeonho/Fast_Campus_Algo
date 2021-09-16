# 근우의 다이어리 꾸미기
# 그리디 또한 규칙을 찾는 것이 중요함

n = input()

check = '1' * len(n)

if len(n) == 1:
    print(1)
elif int(n) >= int(check):
    print(len(n))
else:
    print(len(n)-1)
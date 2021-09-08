# 거스름돈

money = [500, 100, 50, 10, 5, 1]
n = int(input())
change = 1000 - n

cnt = 0
answer = 0
for i in range(len(money)):
    if change >= money[i]:
        cnt = change // money[i]
        change = change % money[i]
        answer += cnt
print(answer)
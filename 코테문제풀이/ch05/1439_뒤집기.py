# 뒤집기

s = input()

answer = 0

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        answer += 1

print((answer+1)//2)
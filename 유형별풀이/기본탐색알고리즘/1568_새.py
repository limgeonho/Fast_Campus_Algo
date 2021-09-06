# 새

n = int(input())
cnt = 0
game = 1
while True:
    if n < game:
        game = 1
    if n == 0:
        break
    n = n - game
    cnt += 1
    game = game + 1
print(cnt)
# 키로거

T = int(input())
for _ in range(T):
    left = []
    right = []
    password = input()
    for p in password:
        if p == '-':
            if left:
                left.pop()
        elif p == '<':
            if left:
                right.append(left.pop())
        elif p == '>':
            if right:
                left.append(right.pop())
        else:
            left.append(p)

    left.extend(reversed(right))

    print(''.join(left))

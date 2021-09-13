# 주사위 네개
# 중복되는 값을 확인 하는 방법은 counter을 사용하는 방법도 있지만 len(set(list())) == <개수>를 통해서 하는 방법도 있다!!

from collections import Counter

T = int(input())
prize = []
for _ in range(T):

    array = list(map(int, input().split()))
    total = 0
    counter = Counter(array)

    if len(counter) == 1:
        tmp = counter.most_common(1)[0][0]
        prize.append(50000 + tmp*5000)
    elif len(counter) == 2:
        if counter.most_common(2)[0][1] == counter.most_common(2)[1][1]:
            tmp = counter.most_common(2)[0][0] + counter.most_common(2)[1][0]
            prize.append(2000 + tmp * 500)
        else:
            tmp = counter.most_common(2)[0][0]
            prize.append(10000 + tmp * 1000)
    elif len(counter) == 3:
        tmp = counter.most_common(1)[0][0]
        prize.append(1000 + tmp*100)
    else:
        tmp = max(array)
        prize.append(tmp * 100)


print(max(prize))

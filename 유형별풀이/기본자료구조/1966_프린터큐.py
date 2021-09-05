# 프린터 큐

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))

    queue = [(value, idx) for idx, value in enumerate(queue)]

    answer = 0

    while True:
        if queue[0][0] == max(queue, key=lambda x:x[0])[0]:
            answer += 1
            if queue[0][1] == m:
                print(answer)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))

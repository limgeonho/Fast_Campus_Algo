# 배
# 박스를 내림차순으로 정렬해서 무거운 순으로 빼는게 최적해

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)
cnt = 0

if boxes[0] > cranes[0]:
    print(-1)
else:
    while boxes:
        cnt += 1
        for i in range(len(cranes)):
            for j in range(len(boxes)):
                if len(boxes) == 0:
                    break
                if cranes[i] >= boxes[j]:
                    boxes.pop(j)
                    break
                else:
                    continue
    if len(boxes) == 0:
        print(cnt)


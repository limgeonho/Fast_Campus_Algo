# 수 찾기
# 존재하는지 여부는 list는 하나하나 확인하지만 set은 바로 확인가능해서 set이 훨씬 빠르다...
n = int(input())

array = set(map(int, input().split()))

m = int(input())

find = list(map(int, input().split()))

for num in find:
    if num in array:
        print(1)
    else:
        print(0)
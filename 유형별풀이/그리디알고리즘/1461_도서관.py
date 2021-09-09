# 도서관
import heapq

n, m = map(int, input().split())

books = list(map(int, input().split()))

positive = []
negative = []

largest = max(max(books), -min(books))

for book in books:
    if book > 0:
        heapq.heappush(positive, -book)
    else:
        heapq.heappush(negative, book)

result = 0

while positive:
    result += heapq.heappop(positive)
    for _ in range(m-1):
        if positive:
            heapq.heappop(positive)

while negative:
    result += heapq.heappop(negative)
    for _ in range(m-1):
        if negative:
            heapq.heappop(negative)

print((-result * 2)-largest)
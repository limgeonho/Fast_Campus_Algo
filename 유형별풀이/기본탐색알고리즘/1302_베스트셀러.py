# 베스트셀러
# target = max(books.values()) => dict의 value값에서 최대값구하기!!!!

n = int(input())
books = {}
for _ in range(n):
    title = input()
    books[title] = books.get(title, 0) + 1

target = max(books.values())

answer = []

for book, cnt in books.items():
    if cnt == target:
        answer.append(book)
answer.sort()
print(answer[0])
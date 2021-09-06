# 문서검색

words = input()
word = input()

print(words.count(word))

# 다른풀이
# index = 0
# result = 0
#
# while len(words) - index >= len(word):
#     if words[index:index + len(word)] == word:
#         result += 1
#         index += len(word)
#     else:
#         index += 1
# print(result)
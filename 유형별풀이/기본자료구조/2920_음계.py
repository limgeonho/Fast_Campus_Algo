# 음계

array = map(str, input().split())

new_array = ''.join(array)

if new_array == '12345678':
    print('ascending')
elif new_array == '87654321':
    print('descending')
else:
    print('mixed')
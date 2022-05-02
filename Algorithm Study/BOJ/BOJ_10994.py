N = int(input())

# 앞 1->5->9
for i in range(1, N):
    cnt = (N - i) * 4 + 1
    print('* ' * (i - 1) + '*' * cnt + ' *' * (i-1))
    print('* ' * i + ' ' * (cnt - 4) + ' *' * i)
# 중간지점
print('* ' * (N * 2 - 1))
# 뒤 9->5->1
for i in range(N-1, 0, -1):
    cnt = (N-i) * 4 + 1
    print('* ' * i + ' ' * (cnt - 4) + ' *' * i)
    print('* ' * (i - 1) + '*' * cnt + ' *' * (i-1))
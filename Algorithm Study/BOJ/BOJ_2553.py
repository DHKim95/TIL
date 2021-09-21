N = int(input())

cnt = 1
for i in range(1, N+1):
    cnt *= i

lst = list(str(cnt))
for i in range(len(lst)-1, -1, -1):
    if lst[i] != '0':
        print(lst[i])
        break
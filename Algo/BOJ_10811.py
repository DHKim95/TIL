N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    sub_arr = arr[a-1:b]
    sub_arr.reverse()
    arr[a-1:b] = sub_arr

for i in arr:
    print(i, end=' ')
N, M = map(int, input().split())

arr = [0 for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    for i in range(a-1, b):
        arr[i] = c

for i in arr:
    print(i, end=' ')
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[0] * (N+1)]

for _ in range(N):
    x = [0] + [int(x) for x in input().split()]
    arr.append(x)

for i in range(1, N+1):
    for j in range(1, N):
        arr[i][j+1] += arr[i][j]

for j in range(1, N+1):
    for i in range(1, N):
        arr[i+1][j] += arr[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(arr[x2][y2] - arr[x1-1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1])
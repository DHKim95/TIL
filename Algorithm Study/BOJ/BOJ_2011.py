N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort()

dp = [1] * N
for i in range(N):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
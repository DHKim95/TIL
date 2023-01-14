N = int(input())

arr = [list(map(int, input().split())) + [0] * (N - (i+1)) for i in range(N)]
dp = [[0] * (N) for _ in range(N)]

dp[0][0] = arr[0][0]
for i in range(1, N):
    for j in range(N):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + arr[i][j]
        elif j == N-1:
            dp[i][j] = dp[i-1][j-1] + arr[i][j]
        else:
            dp[i][j] = max(dp[i-1][j] + arr[i][j], dp[i-1][j-1] + arr[i][j])

print(max(dp[-1]))
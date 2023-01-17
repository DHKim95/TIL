N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            break

        down = i + graph[i][j]
        right = j + graph[i][j]

        if down < N:
            dp[down][j] += dp[i][j]

        if right < N:
            dp[i][right] += dp[i][j]

# print(dp)
print(dp[N-1][N-1])
N, M = map(int, input().split())

square = []

for _ in range(N):
    square.append(list(map(int, input())))

dp = [[0] * (M+1) for _ in range(N+1)]
square_len = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        if square[i-1][j-1] == 1:
            # 길이 계산
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

            # 길이 갱신
            if dp[i][j] > square_len:
                square_len = dp[i][j]

print(square_len ** 2)
T = int(input())

for _ in range(T):
    N = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]

    for i in range(1, N):
        if i == 1:
            dp[0][i] += dp[1][i-1]
            dp[1][i] += dp[0][i-1]
        else:
            # 한칸 대각선이랑 두칸 대각선 비교하기
            dp[0][i] += max(dp[1][i-1], dp[1][i-2])
            dp[1][i] += max(dp[0][i-1], dp[0][i-2])

    # 최대값 찾기
    print(max(dp[0][N-1], dp[1][N-1]))
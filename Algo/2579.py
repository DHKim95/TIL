N = int(input())

stair = [int(input()) for _ in range(N)]
dp = [0] * N

if len(stair) <= 2:
    print(sum(stair))
else:
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
    # 그림그려가며 가질 수 있는 값 가지기
    for i in range(2, N):
        dp[i] = max(stair[i] + stair[i-1] + dp[i-3], stair[i] + dp[i-2])

    print(dp[-1])
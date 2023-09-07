N = int(input())

dp = [0] * (N+1)
dp[0] = 1
# 그전에꺼 곱하기3
for i in range(2, N+1, 2):
    dp[i] = dp[i-2] * 3
    # 점화식대로 곱해주기
    for j in range(0, i-2, 2):
        dp[i] += dp[j] * 2

print(dp[N])

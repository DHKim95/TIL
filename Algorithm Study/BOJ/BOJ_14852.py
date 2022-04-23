N = int(input())

dp = [0 for _ in range(N+1)]

if N == 1:
    print(2)
elif N == 2:
    print(7)
else:
    # 기본 DP
    dp[0] = 1
    dp[1] = 2
    dp[2] = 7

    # 점화식
    for i in range(3, N+1):
        dp[i] = (3 * dp[i-1] + dp[i-2] - dp[i-3]) % 1000000007

    print(dp[N])
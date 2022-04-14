T = int(input()) # 테스트 케이스

dp = [0 for _ in range(1000000)]
dp[0], dp[1], dp[2] = 1, 2, 4

for i in range(3, 1000000):
    dp[i] = ((dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009)

for i in range(T):

    N = int(input())

    print(dp[N-1])
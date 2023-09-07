N, K = map(int, input().split())
coin_lst = []

for _ in range(N):
    coin_lst.append(int(input()))

dp = [0] * (K+1)
dp[0] = 1

for i in coin_lst:
    for j in range(i, K+1):
        dp[j] += dp[j-i]

print(dp[K])